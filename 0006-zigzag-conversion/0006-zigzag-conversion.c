char * convert(char * s, int numRows){
    char conv[1000];
    int i, j, m, n, x, y, gap;
    
    if (numRows == 1)
        return s;
    
    n = numRows - 1;
    m = strlen(s);
    x = 0;
    
    for (i = 0; i < numRows; i++) {
        for (y = i, j = 0; y < m; y += gap, j++) {
            conv[x++] = s[y];
            gap = (n - ((j+1)&1)*(i%n) - (j&1)*((n-i)%n)) << 1;
        }
    }
    
    memcpy(s, conv, m);
    
    return s;
}
