# 「sh generate_folder.sh 番号」 でフォルダを作成
file_names=(A B C D E F G)
mkdir $1
cd $1
for name in "${file_names[@]}"; do
    touch "ABC${1}_${name}.py"
done