import sys                                                                                                                              
from pathlib import Path                                                                                                                   
from numberOfComponentsInADG import UnionFind  # replace with actual class name                                                     
from unionFind import UnionFind                                                                                                         
                                                                                                                                          
                                                                                                                                          
class TestNumberOfComponents:                                                                                                           
      """Group related tests in a class (optional but good for organization)"""                                                           
                                                                                                                                          
      def test_simple_graph(self):                                                                                                        
          # Test with a simple connected graph                                                                                            
          obj = UnionFind()                                                                                                           
          result = obj.method_name(n=5, edges=[[0,1], [1,2], [3,4]])                                                                      
          assert result == 2  # expected: 2 components                                                                                    
                                                                                                                                          
      def test_fully_connected(self):                                                                                                     
          # All nodes connected                                                                                                           
          obj = UnionFind()                                                                                                           
          result = obj.method_name(n=3, edges=[[0,1], [1,2]])                                                                             
          assert result == 1                                                                                                              
                                                                                                                                          
      def test_no_edges(self):                                                                                                            
          # No edges means each node is its own component                                                                                 
          obj = UnionFind()                                                                                                           
          result = obj.method_name(n=4, edges=[])                                                                                         
          assert result == 4                                                                                                              
                                                                                                                                          
      def test_single_node(self):                                                                                                         
          # Edge case: single node                                                                                                        
          obj = UnionFind()                                                                                                           
          result = obj.method_name(n=1, edges=[])                                                                                         
          assert result == 1                                                                                                              
                                                                                                                                          
                                                                                                                                          
  # You can also write standalone test functions (without a class)                                                                        
def test_another_scenario():                                                                                                            
      obj = UnionFind()                                                                                                               
      # your test here                                                                                                                    
      pass                