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

## Screenshot
![Screenshot 2025-02-28 204659](https://github.com/user-attachments/assets/4a3d516d-e2d1-4de8-b3f6-f4bbf1d95a61)

## Mermaid-diagram
![Screenshot 2025-02-28 212738](https://github.com/user-attachments/assets/6907e987-9b2d-407c-a540-878eb7848a2f)
