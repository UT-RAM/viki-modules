/**
  * Ros package to convert a PoseStamped to a Pose
  */


#include <ros/ros.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/PoseStamped.h>

class PoseConverter
{
    private:
    ros::Subscriber pose_stamped_subscriber;
    ros::Publisher pose_publisher;

    public:
    PoseConverter() {
        ros::NodeHandle* nh = new ros::NodeHandle("~");

        pose_stamped_subscriber = nh->subscribe("pose_stamped", 1, &PoseConverter::poseStampedCallback, this);
        pose_publisher = nh->advertise<geometry_msgs::Pose>("pose", 1);
    }

    void poseStampedCallback(const geometry_msgs::PoseStamped pose_stamped_msg)
    {
        pose_publisher.publish(pose_stamped_msg.pose);
    }
};

int main(int argc, char** argv)
{
    ros::init(argc, argv, "pose_stamped_to_pose");
    PoseConverter converter;

    ros::spin();
    return 0;
}