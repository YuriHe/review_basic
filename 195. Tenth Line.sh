# Read from the file file.txt and output the tenth line to stdout.
# 1.Solution, use head tail
head -n 10 file.txt | tail -n +10
# 2.Solution, use awk to get certain text
awk 'NR==10 {print}' file.txt
# 3.Solution use sed(text processing, subtitution, insert, delete, modify)
sed -n '10p' file.txt