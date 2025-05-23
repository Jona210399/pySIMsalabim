"""Compile program with fpc"""
# Description:
# ------------
# Compile program using fpc

import os
import subprocess


def fpc_prog(prog_name,path2prog,show_term_output=True,force_fpc=True,verbose=True):
    """Compile program using fpc

    Parameters
    ----------
    prog_name : str
        Program name (e.g. 'SimSS', 'zimt', 'SIMsalabim)
    path2prog : str
        String of the absolute path to the program
    show_term_output : bool, optional
        show terminal output from the compilation, by default True
    force_fpc : bool, optional  
        force recompile with fpc even if compiled program already exists, by default True
    verbose : bool, optional
        print output of the compilation, by default True
    """   

    is_windows = (os.name == 'nt')          # Check if we are on Windows
    path2prog = str(path2prog)                  # Convert to string
    # Check if the program is already compiled
    if (os.path.isfile(os.path.join(path2prog,prog_name+'.exe')) and is_windows) or (os.path.isfile(os.path.join(path2prog,prog_name)) and not is_windows):
        if force_fpc:
            if show_term_output == True:
                output_direct = None
            else:
                output_direct = subprocess.DEVNULL
            try:
                subprocess.check_call(['fpc', prog_name.lower()+'.pas'], encoding='utf8', stdout=output_direct, cwd=path2prog, shell=is_windows)
            except subprocess.CalledProcessError:
                print('Error compiling '+prog_name+' in '+path2prog)
                raise ChildProcessError
            if verbose:
                print('\n'+prog_name+' already existed but was recompiled'+'\n')
        else:
            if verbose:  
                print('\n'+prog_name+' already compiled')
    
    else: # Compile the program
        if show_term_output == True:
            output_direct = None
        else:
            output_direct = subprocess.DEVNULL
        try:
            subprocess.check_call(['fpc', prog_name.lower()+'.pas'], encoding='utf8', stdout=output_direct, cwd=path2prog, shell=is_windows)
            if verbose:
                print('\n'+prog_name+' was not compiled so we did it!'+'\n')
        except subprocess.CalledProcessError:
            print('Error compiling '+prog_name+' in '+path2prog)
            raise ChildProcessError    

    