void setZeroes(int** matrix, int matrixSize, int* matrixColSize){

    int auxmat[matrixSize][(*matrixColSize)]; //auxmat is an auxillary matrix
    int i,j,k;
    for(i=0;i<matrixSize;i++)
    {
        for(j=0;j<*(matrixColSize);j++)
        {
            auxmat[i][j]=matrix[i][j];
        }
    }
    for(i=0;i<matrixSize;i++)
    {
        for(j=0;j<(*matrixColSize);j++)
        {
            if(matrix[i][j]==0)
            {
                for(k=0;k<matrixSize;k++)
                {
                    auxmat[k][j]=0;
                }
                
                for(k=0;k<(*matrixColSize);k++)
                {
                    auxmat[i][k]=0;
                }
            }
        }
    }
    for(i=0;i<matrixSize;i++)
    {
        for(j=0;j<(*matrixColSize);j++)
        {
            matrix[i][j]=auxmat[i][j];
        }
    }
}