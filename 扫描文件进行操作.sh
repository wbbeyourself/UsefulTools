#!/bin/bash
# 改变的参数
model="base"
codep="~/blstm-crf-csc"
#codep="~/xxx-lattice"
#codep="~/xxx-guniform"
srcp="~/data/error-type"

# 一些固定的路径
dstp="$srcp-predict"
dstp="$dstp/$model"
mkdir -p $dstp
modelp="~/data/model/$model/all/best"
msetp="~/data/model/$model/all/m.dset"

export CUDA_VISIBLE_DEVICES=0
source deactivate
source activate lattice

# 对一个文件夹里的文件进行同样的操作
# 用到了 for 循环
files=`ls $srcp`
for i in $files
do
    fi="$srcp/$i"
    tgt="$dstp/$i-p"
    log="/tmp/abc"
    
    
    # 预测
    sleep 2s
    echo $fi
done


