Files="auto93 china coc1000 coc10000 diabtes healthCloseIsses12mths0001-hard healthCloseIsses12mths0011-easy nasa93dem pom soybean"
for f in $Files do
    curl https://github.com/timm/lo/blob/6jan24/data/$f.csv
done