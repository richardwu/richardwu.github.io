declare -A terms

twob=(co250 math239 stat231)
threec=(stat331 stat333 math247)

terms[2b]=twob[@]
terms[3a]=threec[@]

base="$HOME/Dropbox/uni-courses"
suffixes=("-notes.pdf" "-final-notes.pdf")

for term in ${!terms[@]}; do
  for suffix in ${suffixes[@]}; do
    term_courses=${!terms[${term}]}
    for course in ${term_courses[@]}; do
      dest="${course}${suffix}"
      source="$base/$term/$course/$dest"
      if [ -f $dest ]; then
        echo "skip $dest (file exists)"
      else
        echo "ln $source $dest"
        ln $source $dest
      fi
    done
  done
done
