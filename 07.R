dat <- scan('07.txt', sep=',')

fuel_to_p1 = 0
for ( i in 1:length(dat) )
{
    fuel_to_p1 <- fuel_to_p1 + abs(dat[i] - median(dat))
}

fuel_to_p2 = 0
for ( i in 1:length(dat) )
{ for ( j in 1:(abs(dat[i] - floor(mean(dat)))) )  # Not sure why floor was needed, but it works.
    {
       fuel_to_p2 <- fuel_to_p2 + j
    }
}
print(fuel_to_p1)
print(fuel_to_p2)
