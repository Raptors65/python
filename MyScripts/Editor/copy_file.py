# From https://forum.omz-software.com/topic/4560/copyfile-action

from shutil import copyfile
import editor

copyfile(editor.get_path(),editor.get_path().split(".")[0].split("/")[-1]+'.copy')
