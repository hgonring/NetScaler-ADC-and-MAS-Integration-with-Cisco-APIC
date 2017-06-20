# Scenario 1. APIC System Overview and Operations #

This scenario provides an overview of the APIC System Health dashboard and how to drill down into a health score to identify a root issue.

## Steps ##

1. From the demo workstation, open **Application Policy Infrastructure Controller** (if it is not already open) by clicking the **APIC Login** icon , and login (**admin/C1sco12345/Advanced**).

2. Click **NO** on the Warning pop-up.

	![Popup1](images/Popup.png)

3. Click **Tenants** in the top menu, then click **common** in the sub menu.

4. Point out the sections of the APIC dashboard.

	* The top of the GUI screen is the Menu bar tab.
	* The middle of the GUI is the Submenu bar tab.
	* The bottom left of the GUI screen is the Navigation Pane.
	* The middle-right of the GUI is the Work Pane.
	* The menu bar within the work pane shows the Tabs.

![Screenshot](images/Screenshot1.png)

### System Health Dashboard ###

1. From the menu bar, click **System** to display the **System Health Dashboard**.
  
    * Explain that you logged in with global administrative rights and your view includes   all system components.
    * Show the single-pane view, which provides a centralized, application-level  visibility with real-time application health monitoring across the physical and  virtual environments.
    * Show the health scores and explain how a health score is displayed for components   that are being monitored by APIC, such as:
    	* Fabric health
    	* Connections to virtual and physical environments
    * Show that the left pane contains health scores for the overall system as well as  specific components.
    * Show that the right pane contains fault counts based on areas that have errors.
    ![Screenshot](images/Screenshot2.png)

2. Double-click **Leaf1**, which has a health score of 90.

3. In the Leaf1 window, click the **Health** tab and scroll down until the element with a health score of 90 or lower becomes visible.
  ![Screenshot](images/Screenshot3.png)

4. Click the + sign to expand the Equipment Policy to view the Power Supply that is showing a fault.
  ![Screenshot](images/Screenshot4.png)
 
5. Right-click the Power Supply Group and click Show Faults in the resulting menu.
  ![Screenshot](images/Screenshot5.png)
 
6. Examine the resulting table, which shows the details of the fault.
  ![Screenshot](images/Screenshot6.png)

7. Close the **Show Fault**s window.

### Visibility & Troubleshooting ###

1. Click **Operations** to get to the Troubleshooting Wizard View.
  ![Screenshot](images/Screenshot7.png)

2. In the Session Name field, type **tsw_session1**.

3. In the Description field, type **Troubleshooting Session 1**.

4. In the Source field, type the source IP address: **10.193.101.14** and click **Search**. Click the result.

5. In the Destination field, type the destination IP address: **10.193.102.17** and click **Search**. Click the result.
  ![Screenshot](images/Screenshot8.png)
 
6. In the **Time Window**, either use the drop-down to choose a number of minutes for the session, or check the **Use fixed time** checkbox and select any **From**: and **To**: times in the Time Window drop-downs and click the **Start** button.
The APIC will start the live troubleshooting and build the logical topology based on source and destination.

#### Troubleshooting Session ####

The system displays a logical topology based on the previously entered source and destination information.

1. Click any yellow icon to see the specific fault on the topology.
  ![Screenshot](images/Screenshot9.png)
 
2. To see all the faults, click the List icon at the top left of the work pane.
  ![Screenshot](images/Screenshot10.png)
 
#### Drops/Stats ####

In this section you can see any packet drops on the logical topology.

1. Click **Drop/Stats** in the side menu.

2. Review the logical topology, which is similar to the earlier display in the Topology window.
  ![Screenshot](images/Screenshot11.png)

3. Click any yellow icons with the down arrow to see the statistics on that device / node.
  ![Screenshot](images/Screenshot12.png)
 
#### Contracts ####

Contracts are enforced between EPGs (End Point Groups). Bi-directional contracts are shown in the figure below.

![Screenshot](images/Screenshot13.png)

1. Click **Contracts** on the side menu.

2. The **Source Endpoint to Destination Endpoint** box shows the contracts, including filters with node IDs and hit counts.

3. The **Destination Endpoint to Source Endpoint** box shows the same information in the reverse direction.

#### Traceroute ####

The purpose of this section is to run fabric-aware traceroute on multipath based on the direction and protocols.

>**NOTE**: In a real Cisco ACI Fabric you should see traceroute **GREEN** from leaf1 all the way to destination host for Source to Destination and vice versa. The APIC Simulator only shows traceroute from the Spines.

1. Click **Traceroute** in the side menu.

2. Select ICMP from the Protocol drop-down and click the Play button to start the traceroute, then click **OK**.

3. A **GREEN** path from the source to the destination is displayed, because no issues are present.

  ![Screenshot](images/Screenshot14.png)

#### Atomic Counter ####

The Atomic Counter counts packets and bytes between source and destination. Only packets that traverse the fabric are counted. Locally switched packets are not counted.

1. Click **Atomic Counter** in the side menu.

2. Click **Play** to start the below shows Ongoing Counters. Click **OK**.

3. Wait approximately two minutes for the counter table to generate.

  ![Screenshot](images/Screenshot15.png)
