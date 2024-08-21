#include <iostream>
using namespace std;

int arr[1000][1000] = {0};
int dfs[1000] = {0};
int bfs[1000] = {0};

void f_dfs(int v, int n){
    dfs[v] = 1;
    cout << v + 1 << " ";

    for(int i = 0; i < n; i++){
        if(arr[v][i] == 1 && dfs[i] == 0){
            f_dfs(i, n);
        }
    }
}

void f_bfs(int v, int n){
    int que[n] = {0};
    int front = -1;
    int rear = -1;

    do{
        cout << v + 1 << " ";
        bfs[v] = 1;

        for(int i = 0; i < n; i++){
            if(arr[v][i] == 1 && bfs[i] == 0){
                que[++rear] = i;
                bfs[i] = 1;
            }
        }

        v = que[++front];
    } while (front <= rear);

}

int main() {
   int n, m, v;
   cin >> n >> m >> v;

   int start, end;

   for(int i = 0; i < m; i++){
      cin >> start >> end;
      arr[start - 1][end - 1] = 1;
      arr[end - 1][start - 1] = 1;
   }

   f_dfs(v - 1, n);

//    for(int i = 0; i < n; i++){
//     if(dfs[i] == 0){
//         f_dfs(i, n);
//     }
//    }

   cout << endl;

   f_bfs(v - 1, n);

}