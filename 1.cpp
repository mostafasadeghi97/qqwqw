
#include<algorithm>
#include<string>
#include<cmath>
#include <numeric>
#include <vector>
#include <iostream>
#include <iterator>



//================= MOSTAFA SADEGHI   9423067 ================

using namespace std::rel_ops;



int main() { 
	
	
	std::vector<int> vec1( 100 );
	std::iota( std::begin( vec1 ), std::end( vec1 ), 1 );
	std::vector<int> vec2( 10 );
	std::iota( std::begin( vec2 ), std::end( vec2 ), 1 );
	vec2.insert(vec2.end(), vec1.begin(), vec1.end());
	std::vector<int> odd_vec;
	copy_if(vec1.begin(), vec1.end(), std::back_inserter(odd_vec), [](const int i) { return i % 2 == 1; });
	std::vector<int> reverse_vec(vec1.rbegin(), vec1.rend());
	// for (size_t i = 0; i < reverse_vec.size(); i++)
	// {
	// 	std::cout << reverse_vec[i] << std::endl;
	// }
	// sort(vec2.begin(), vec2.end());
	// sort(std::execution::par, vec2.begin(), vec2.end());
	std::copy(vec2.begin(), vec2.end(), std::ostream_iterator<int>(std::cout, "\n"));
	
	

	return 0;
} 
