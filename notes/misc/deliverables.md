# Deliverables
# 3/30/31
1. finish array bit:
    2. bars
    3. histogram
        * Drawstyles PR
            * histogram can take in 2 1D vectors that are different sizes:
                * need to access both the values and the bins 
2. restructure above w/ query_metadata idea
3. Do array & dataframe in parallel 



|   | shape constraints| array | dataframe |
| -------- | -------- | -------- |---|
| LineCollection| unique ($\vec{X},\vec{Y}$) pairs <br/>([N0....Nn], [N0...Nn]) |     |       |
| BarCollection |  position, heights(can be many)<br/> (N, [N...N])|   |      |
|HistCollection | bin_edges, bin_values<br/> (N+1, [N...N])||

[N...N] means $N_{i}\in N$ are of same length

