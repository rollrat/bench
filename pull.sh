mkdir $2
mkdir $2/07
mkdir $2/08
mkdir $2/09
mkdir $2/10

scp RDMA-07:~/$1/* $2/07
scp RDMA-08:~/$1/* $2/08
scp RDMA-09:~/$1/* $2/09
scp RDMA-10:~/$1/* $2/10
