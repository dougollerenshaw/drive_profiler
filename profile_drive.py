import os
import pandas as pd
import time
import datetime
import click

class DriveProfiler(object):
    def __init__(self,path_to_profile):
        self.top_level_path = path_to_profile
        t0 = time.time()
        self.summary = self.run_profile(self.top_level_path)
        self.time_to_profile = time.time()-t0

    def run_profile(self,start_path = '.'):
        size_dict_list = []
        for dirpath, dirnames, filenames in os.walk(start_path):
            dirsize = 0
            for f in filenames:
                dirsize += os.path.getsize(os.path.join(dirpath, f))
            size_dict_list.append({'fullpath':dirpath,
                                'foldername':os.path.split(dirpath)[-1],
                                'size_bytes':dirsize,
                                'size_kb':int(dirsize/(2.**10)),
                                'size_mb':int(dirsize/(2.**20)),
                                'size_gb':int(dirsize/(2.**30))})
        return pd.DataFrame(size_dict_list)


@click.command()
@click.option('--path', default='pwd', help='path to profile. Default is the current directory')
@click.option('--savepath', default='profile_path', help='path to save profile results. Default is directory being profiled')
def main(path,savepath=None,filename='folder_profile'):
    if path == 'pwd':
        path = os.getcwd()
    if savepath == 'profile_path':
        savepath = path

    assert os.path.exists(path), "profile path doesn't exist"
    assert os.path.exists(savepath), "savepath doesn't exist"

    # run profile
    print('Profiling {}...'.format(path))
    profile = DriveProfiler(path)

    # get timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%I.%M.%S%p')

    # save results
    if savepath is not None:
        savepath_full = os.path.join(savepath,'profile_results_{}.csv'.format(timestamp))
        print('Done. Saving results to {}'.format(savepath_full))
        total_size_mb = profile.summary['size_bytes'].sum()/(2.**20)
        print('The total size of all folders in this drive is {} MB'.format(total_size_mb))
        profile.summary.sort_values(by=['size_bytes'],ascending=False).to_csv(savepath_full,index=False)

if __name__ == '__main__':
    main()