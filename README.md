# PyKDL_without_ros

Ros연동 없는 Python3 버전 PyKDL 사용방법입니다.

사용 전에 PyKDL.so 파일을 빌드하여  python3 dist-package폴더에 넣어야합니다.

# PyKDL.so 빌드방법
```bash 
git clone https://github.com/liruiw/orocos_kinematics_dynamics/tree/cfaf8ab13f58fd64ef238c89c497f37f86619f29

cd orocos_kinematics_dynamics
cd sip-4.19.3
python3 configure.py 
make -j16; sudo make install
 
export ROS_PYTHON_VERSION=3
cd ../orocos_kdl
mkdir build; cd build;
cmake ..
make -j8; sudo make install
  
cd ../../python_orocos_kdl
mkdir build; cd build;

cmake-gui .. >> change orocos_kdl ligraries location


cmake ..  -DPYTHON_VERSION=3.6.9 -DPYTHON_EXECUTABLE=PYTHONPATH
make -j8;  cp PyKDL.so /usr/local/lib/python3.5/dist-packages/
```
# TEST RESULT
```bash
random joint angle :  [-1.85521104  0.30567292  0.94301279  0.02044278  0.08270382 -1.05178842]
pose :  [[ 0.64296763  0.59471056  0.48260955 -0.16975677]
 [-0.72802558  0.27888986  0.62625809  0.04587408]
 [ 0.23784739 -0.75401578  0.61228165  0.72832061]
 [ 0.          0.          0.          1.        ]]
(3, 1)
inverse_kinematics :  [-1.85520767  0.30567353  0.94312498  0.02044259  0.08258842 -1.05178724]
pose sol:  [[ 0.64296763  0.59471056  0.48260955 -0.16975677]
 [-0.72802558  0.27888986  0.62625809  0.04587408]
 [ 0.23784739 -0.75401578  0.61228165  0.72832061]
 [ 0.          0.          0.          1.        ]]
pose:  [[ 0.64296763  0.59471056  0.48260955 -0.16975677]
 [-0.72802558  0.27888986  0.62625809  0.04587408]
 [ 0.23784739 -0.75401578  0.61228165  0.72832061]
 [ 0.          0.          0.          1.        ]]
sum of pose_error :  4.271873840777651e-09
Jacobian of q :  [[-4.58740820e-02 -5.50575998e-01  4.68956179e-03  1.74534945e-01
   6.93889390e-18  0.00000000e+00]
 [-1.69756766e-01  1.60955490e-01  3.79993711e-03 -2.34566094e-01
   2.08166817e-17  0.00000000e+00]
 [ 0.00000000e+00 -1.75809037e-01  1.08393285e-03  6.72034257e-02
   8.67361738e-19  0.00000000e+00]
 [ 0.00000000e+00 -2.80595725e-01 -2.88845222e-01  7.64717895e-01
  -2.77010664e-01  6.42967626e-01]
 [ 0.00000000e+00 -9.59826046e-01  8.44410659e-02  6.19648497e-01
   6.84725409e-02 -7.28025584e-01]
 [ 1.00000000e+00  0.00000000e+00  9.53644664e-01  1.76754862e-01
   9.58424021e-01  2.37847389e-01]]
```
