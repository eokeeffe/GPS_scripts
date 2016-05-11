#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

template<typename T>
std::vector<double> linspace(T start_in, T end_in, int num_in)
{
  double start = static_cast<double>(start_in);
  double end = static_cast<double>(end_in);
  double num = static_cast<double>(num_in);
  double delta = (end - start) / (num - 1);

  std::vector<double> linspaced(num - 1);
  for(int i=0; i < num; ++i)
    {
      linspaced[i] = start + delta * i;
    }
  linspaced.push_back(end);
  return linspaced;
}

vector<pair<double,double> > meshgrid(double min_x,double min_y,double max_x,double max_y,int cell_size)
{
    vector<double> x = linspace(min_x,max_x,cell_size);
    vector<double> y = linspace(min_y,max_y,cell_size);
    
    int num_rows=x.size();
    int num_cols=y.size();
    
    cout<<num_rows<<endl;
    cout<<num_cols<<endl;
    
    vector<pair<double,double> > mesh;
    for(int i=0;i<x.size();i++)
    {
        for(int j=0;j<y.size();j++)
        {
            mesh.push_back(make_pair(x[i],y[j]));
        }
    }
    return mesh;
}
/*
vector<pair<double,double> > max_grid(vector<pair<double,double> > points)
{
    vector<pair<double,double> points;
}
*/
int main(int argc,char *argv[])
{
    vector<pair<double,double> > map = meshgrid(53.306938,-6.231533,
    53.307655,-6.233088,5);
    for(int i=0;i<map.size();i++)
    {
        std::pair<double,double> p = map[i];
        cout<<p.first<<","<<p.second<<endl;
    }
    cout<<map.size()<<endl;
    return 0;
}
