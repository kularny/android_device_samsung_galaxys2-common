import common
import struct

def FullOTA_PostValidate(info):
	# run e2fsck
	info.script.AppendExtra('run_program("/sbin/e2fsck", "-fy", "/dev/block/mmcblk0p9");');
	# resize2fs: run and delete
	info.script.AppendExtra('run_program("/sbin/resize2fs", "/dev/block/mmcblk0p9");');
	# run e2fsck
	info.script.AppendExtra('run_program("/sbin/e2fsck", "-fy", "/dev/block/mmcblk0p9");');
