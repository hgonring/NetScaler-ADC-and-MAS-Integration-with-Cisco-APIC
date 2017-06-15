## Scenario 1. APIC System Overview and Operations ##


	![Popup1](images/Popup.png)

3. Click **Tenants** in the top menu, then click **common** in the sub menu.

	* The middle-right of the GUI is the Work Pane.
	* The menu bar within the work pane shows the Tabs.

![Screenshot](images/Screenshot1.png)

### System Health Dashboard ###

  * Explain that you logged in with global administrative rights and your view includes all system components.
  * Show the single-pane view, which provides a centralized, application-level visibility with real-time application health monitoring across the physical and virtual environments.
  * Show the health scores and explain how a health score is displayed for components that are being monitored by APIC, such as:
  		* Fabric health
  		* Connections to virtual and physical environments
  * Show that the left pane contains health scores for the overall system as well as specific components.


 ![Screenshot](images/Screenshot2.png)

2. Double-click **Leaf1**, which has a health score of 90.

 ![Screenshot](images/Screenshot3.png)

4. Click the + sign to expand the Equipment Policy to view the Power Supply that is showing a fault.

 ![Screenshot](images/Screenshot4.png)
 
5. Right-click the Power Supply Group and click Show Faults in the resulting menu.

 ![Screenshot](images/Screenshot5.png)
 
6. Examine the resulting table, which shows the details of the fault.

 ![Screenshot](images/Screenshot6.png)




 ![Screenshot](images/Screenshot7.png)

2. In the Session Name field, type **tsw_session1**.

 ![Screenshot](images/Screenshot8.png)
 
6. In the **Time Window**, either use the drop-down to choose a number of minutes for the session, or check the **Use fixed time** checkbox and select any **From**: and **To**: times in the Time Window drop-downs and click the click the **Start** button.


#### Troubleshooting Session ####


 ![Screenshot](images/Screenshot9.png)
 


 ![Screenshot](images/Screenshot10.png)
 
#### Drops/Stats ####

 
  ![Screenshot](images/Screenshot11.png)

3. Click any yellow icons with the down arrow to see the statistics on that device / node.

 ![Screenshot](images/Screenshot12.png)
 
#### Contracts ####


![Screenshot](images/Screenshot13.png)

1. Click **Contracts** on the side menu.

#### Traceroute ####

>**NOTE**: In a real Cisco ACI Fabric you should see traceroute **GREEN** from leaf1 all the way to destination host for Source to Destination and vice versa. The APIC Simulator only shows traceroute from the Spines.

1. Click **Traceroute** in the side menu.
2. Select ICMP from the Protocol drop-down and click the Play button to start the traceroute, then click **OK**.

 ![Screenshot](images/Screenshot14.png)

#### Atomic Counter ####


 ![Screenshot](images/Screenshot15.png)
 

 
 

