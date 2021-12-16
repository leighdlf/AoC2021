# Read data from imput, and set up which points to mark, and which axis and position to fold.
library(stringr)
dat <- readLines('data/13.txt')
points <- str_match(dat, "(?<y>[0-9]+)[,](?<x>[0-9]+)")[, -1] |> na.omit(points)
fold <- str_match(dat, "(?<axis>[xy])[=](?<line>[0-9]+)")[, -1] |> na.omit(fold)

# Setting up the paper.
if (fold[1, 1] == 'x') { colsize <- (as.numeric(fold[1, 2])*2) + 1; rowsize <- (as.numeric(fold[2, 2])*2) + 1 } # The fold is always in the middle.
if (fold[1, 1] == 'y') { colsize <- (as.numeric(fold[2, 2])*2) + 1; rowsize <- (as.numeric(fold[1, 2])*2) + 1 } # Aditional +1 (and some additions later) is to compensate for non-0 indexing.
paper <- matrix(F, nrow = rowsize, colsize)

# Marking the paper.
for (row in 1:nrow(points)) {
        x <- as.numeric(points[row,]['x']) + 1
        y <- as.numeric(points[row,]['y']) + 1
        paper[x, y] <- T
}

# Main function for folding the paper.
fold_paper <- function(paper, fold, i) {

    if (fold[, 'axis'][i] == 'y') {
        fold_y <- paper[(as.numeric(fold[,'line'][i]) + 2):nrow(paper),] # Bottom
        folded_y <- paper[1:(as.numeric(fold[,'line'][i])),] # Top
        for (row in 1:nrow(fold_y)) {
            for (col in 1:ncol(fold_y)) {
                if (folded_y[row, col] == F) {
                    folded_y[row, col] <- fold_y[1 + nrow(fold_y) - row, col]
                    paper <- folded_y
                }       
            }
        }
    } 
    else {
        fold_x <- paper[,1:(as.numeric(fold[,'line'][i]))] # Left side
        folded_x <- paper[,(as.numeric(fold[,'line'][i]) + 2):ncol(paper)] # Right side
        for (row in 1:nrow(fold_x)) {
            for (col in 1:ncol(fold_x)) {
                if (folded_x[row, col] == F) {
                    folded_x[row, col] <- fold_x[row, 1 + ncol(fold_x) - col]
                    paper <- folded_x
                }       
            }
        }
    }
    # Part 1
    if (fold[, 'axis'][1] == 'y') {
        sum(folded_y))

        } else {
        sum(folded_x))
        }
    return (paper)
}

# Loop to fold the paper for each fold instruction.
for (i in 1:nrow(fold)) {
    paper <- fold_paper(paper, fold, i)
}

# Convert from a bool matrix to something more readable, then export to a csv file.
p_paper <- matrix(' ', nrow = nrow(paper), ncol(paper))
for (row in 1:nrow(paper)) {
    for (col in 1:ncol(paper)) {
        if (paper[row, col] == T) {
            p_paper[row, col] <- '#'
        }
    }     
}
print(p_paper)
write.csv(p_paper,file="paper.csv")
