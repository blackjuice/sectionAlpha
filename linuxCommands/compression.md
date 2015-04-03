## TAR.GZ [(source)](http://www.simplehelp.net/2008/12/15/how-to-create-and-extract-zip-tar-targz-and-tarbz2-files-in-linux/)

Good compression while not utilizing too much of the CPU.

`tar -zcvf archive_name.tar.gz directory_to_compress`

To decompress an archive use the following syntax:

`tar -zxvf archive_name.tar.gz`

Extract the files to a different directory:

`tar -zxvf archive_name.tar.gz -C /tmp/extract_here/`

## Extracting general .tar balls

`tar xf archive.tar`
