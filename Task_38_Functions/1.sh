function read_file() {
    if [[ -r $1 ]]
    then
        wc -l $1
    else
        echo -1
    fi
}

read_file $1