#include<iostream>
#include <list>
#include <vector>
#include <stack>
#include <fstream>

using namespace std;

struct Graph{

    int V;
    vector<list<int> > adj;
    vector<vector<int> > convert(int V);
    void Criar(int NumVert);
    void addEdge(int v, int w);
    void BuscaLargura(int s);
    void BuscaProfundidade(int s);
    void addVertex();
    void printGraph(int V);
    void AdjMatrix(vector<vector<int> > adj, int v);
    void BuscaVerticie (int V);
};

void Graph::Criar(int NumVert){
    V = NumVert;
    adj.resize(size_t(NumVert));
}


void Graph::addEdge(int u, int v){
    adj[u].push_back(v);
    adj[v].push_back(u);
}

void Graph::addVertex(){
    adj.push_back(list<int>());
}

vector<vector<int> > Graph::convert(int V){

    vector<vector<int> > matrix(V, vector<int>(V, 0));

    for (int i = 0; i < V; i++) {
        for (auto j : adj[i])
            matrix[i][j] = 1;
    }
    return matrix;
}

void Graph::AdjMatrix(vector<vector<int> > adj, int V){
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cout << adj[i][j] << "   ";
        }
        cout << endl;
    }
    cout << endl;
}

void Graph::BuscaVerticie(int V){
    for (int x : adj[V]){
        cout << x;
    }
    cout<<"\n";
}


void Graph::BuscaLargura(int s){
    bool *descoberto = new bool[V];
    for(int i = 0; i < V; i++)
        descoberto[i] = false;

    list<int> queue;

    descoberto[s] = true;
    queue.push_back(s);

    list<int>::iterator i;

    while(!queue.empty()){
        s = queue.front();
        cout << s << " ";
        queue.pop_front();

        for (i = adj[s].begin(); i != adj[s].end(); ++i){
            if (!descoberto[*i]){
                descoberto[*i] = true;
                queue.push_back(*i);
            }
        }
    }
    cout << endl;
}

void Graph::BuscaProfundidade(int s){

    vector<bool> descoberto(V, false);

    stack<int> stack;

    stack.push(s);

    while (!stack.empty()){

        s = stack.top();
        stack.pop();

        if (!descoberto[s]){
            cout << s << " ";
            descoberto[s] = true;
        }


        for (list<int>::iterator i = adj[s].begin(); i != adj[s].end(); ++i)
            if (!descoberto[*i])
                stack.push(*i);
    }
}

int main()
{
    ifstream filein;
    int tamanho=0, i, verticie;
    Graph g;
    filein.open("num.txt");
    filein>>tamanho;
    g.Criar(tamanho);
    int vet[3];

    while(!filein.eof()){
        for(i=0;i<3;i++){
        filein>>vet[i];
        }
        g.addEdge(vet[0], vet[1]);
    }


    vector<vector<int> > Matrix = g.convert(tamanho);

     cout << "Matriz de adjacencia: \n";
    g.AdjMatrix(Matrix, tamanho);

    cout << "entre com o numero de verticie\n";
    cin >> verticie;
    g.BuscaVerticie(verticie);

    cout << "Percurso em largura "<<endl;
        g.BuscaLargura(0);

    cout << "Percurso em profundidade "<<endl;
        g.BuscaProfundidade(0);

    cout << endl;


    return 0;
}
