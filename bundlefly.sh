# ------------- path settings --------------- #
ROOT_FILE=F:/PycharmProjects/bundlefly
CONFIG_FILE=${ROOT_FILE}/bundlefly_config
BUNDLEFLY_00_FILE=${CONFIG_FILE}/bundlefly_00
BUNDLEFLY_01_FILE=${CONFIG_FILE}/bundlefly_01


# ------------- bundlefly 00 p=k/3 ---------- #
for file in `ls ${BUNDLEFLY_00_FILE}` ; do
    ./booksim ${BUNDLEFLY_00_FILE}/$file
done

sleep 1000000