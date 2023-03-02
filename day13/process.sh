
sed 's/lose /-/g;s/gain //g;s/\.//g' input.txt > temp.txt
awk '{printf $1" "$10" "$3"\n" > "proc.txt"}' temp.txt && rm temp.txt