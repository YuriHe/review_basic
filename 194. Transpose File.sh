# Read from the file file.txt and print its transposed content to stdout.
# !bin/bash
# t[1] = "name alice ryan" t[2] = "age 21 30"
awk '
{
    for (i=1; i <= NF; i++) {
        if (NR == 1) {
            t[i] = $i
        } else {
            t[i] = t[i] " " $i
        }
    }
}
END {
    for (i=1; i<= NF; i++){
        print t[i]
    }
}
' file.txt