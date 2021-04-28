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
