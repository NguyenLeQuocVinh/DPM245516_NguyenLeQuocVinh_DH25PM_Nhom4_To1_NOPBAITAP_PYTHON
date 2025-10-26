import time
import os

hinh1 = """
    *        
   * *
  *   *
 *     *
*********
"""

hinh2 = """
*******
*     *
*     *
*     *
*******
"""

hinh3 = """
*******
*      
*      
*      
*******
"""

hinh4 = """
*******
*     *
*     *
*******
*     *
*     *
*******
"""


ds_hinh = [hinh1, hinh2, hinh3, hinh4]


for h in ds_hinh:
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(h)
    time.sleep(5)  # Dừng 5 giây trước khi hiện hình tiếp theo
