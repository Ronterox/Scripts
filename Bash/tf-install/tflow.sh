#!/bin/bash

input() {
    echo '----------------------------------------------'
    echo "$1"
    while [ "$ans" != 'y' ] && [ "$ans" != 'n' ] ; do
        read -p 'y/n: ' ans
    done
    [ "$ans" == 'y' ] && make $2
    ans=0
}

input 'Update?' update

input 'Download conda?' condadownload

source ~/.bashrc && conda -V

input 'Create conda env?' condaenv

input 'Install conda-forge?' condaforge

input 'Set path?' condapath

input 'Pip upgrade and install tflow?' tensorflow

input 'Test CPU?' tfcpu

input 'Test GPU?' tfgpu
