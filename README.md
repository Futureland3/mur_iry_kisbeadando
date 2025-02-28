# `mur_iry_kisbeadando` package
ROS 2 C++ package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)

"A package egy node-ból áll. A /draw_house node a turtlesim szimulátorban képes egy ház alakzatot kirajzolni. A mozgást a /turtle1/cmd_vel topicon keresztül hirdeti, míg a teleportálást és a tollvezérlést a /turtle1/teleport_absolute és /turtle1/set_pen szolgáltatásokkal végzi. Megvalósítás ROS 2 Humble alatt."

## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/Futureland3/mur_iry_kisbeadando
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select mur_iry_kisbeadando --symlink-install
```

<details>
<summary> Don't forget to source before ROS commands.</summary>

``` bash
source ~/ros2_ws/install/setup.bash
```
</details>

``` r
ros2 launch mur_iry_kisbeadando house_launch.py
```