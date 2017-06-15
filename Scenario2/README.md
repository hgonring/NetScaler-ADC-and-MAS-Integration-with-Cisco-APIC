## Scenario 2. Single-Tenant with a Single-Node Graph via the Northbound API

![Figure1](images/Figure1.png)

> NOTE: The Python script method calls individual XML scripts to create a series of objects. To pause the script and create an object using an APIC wizard, see the instructions inline. Objects that can be created via wizard using this script are indicated with (*) in the list below.



* Creates a Tenant



Method  | Automation Level | Explanation   | Completion Time | Notes
------------- | ------------- | ------------- | -------------   |------------- 
Use Python Scripting to Build Objects Within the APIC  | High |  To configure the APIC objects with scripts, the user downloads a set of configuration scripts and employs them in a command window, monitoring the output via the APIC UI.| 20 minutes      | To maximize the effectiveness of this Scenario, view the relevant directories in APIC while the Python scripts are working, to show the discovery of the network objects in real-time.
Manual Configuration of Individual Objects  | Low  | Use an APIC wizard and the configuration parameters provided in this script to manually create each required object| 60 minutes      | See the links in each step to the procedure for manual object creation.

### Steps 

1. From the demonstration workstation, go to the open **Application Policy Infrastructure Controller** window.


 ![Figure2](images/Figure2.png)
6. Login to PuTTy (**user01/user01**) and place it so that both the PuTTY window and the APIC directories are visible.
 ![Figure3](images/Figure3.png)
7. From the command line type **./request.py Citrix_Scripts/Build_Citrix_VPX.cfg** and hit **<Enter>**. 
> NOTE: To show the XML code as the Python script calls each XML script, substitute
 ![Figure4](images/Figure4.png)
> This is an example of the partial XML output for the **Build_Citrix_VPX.xml** script. 

	The Build_Citrix_VPX.cfg script utilizes a series of XML scripts to perform the necessary configuration steps. It will pause between each of the XML scripts, and the user can either press <Enter> to run the script, or type s to skip the script
![Figure5](images/Figure5.png)
>The following step creates the tenant in APIC. To perform this procedure manually, type s and hit enter at the prompts for the 1N_Tenant.xml script.

8. Create the **Tenant**.

 	a. In the APIC top menu, select **Tenants**. Select **ALL TENANTS** from the top sub-menu.
 	![Figure6](images/Figure6.png)
 	
 	b. Return to the PuTTY window and hit **Enter** at the Hit return to process **Citrix_Scripts/1N_Tenant.xml or press‘s’ and return to skip this script** prompt.
 	
	![Figure7](images/Figure7.png)

	d. Double-click the newly created **Visa** tenant.
	
9. Import the **Citrix Device Package** as follows:
	
	a. From the top menu, select **L4-L7 Services**.
	
	
	
	d. Return to the PuTTY window and hit <**Enter**> at the **Hit return to process Citrix_Scripts/DevicePackage-11.0-65.36.zip or press‘s’ and return to skip this script** prompt.
	
	![Figure8](images/Figure8.png)
> NOTE: The next three steps create the device cluster, concrete devices and logical interfaces in the APIC. To create these devices manually, type s and hit enter at the prompts for the following scripts:
>


10. Create the Device Cluster:
	
	a. From the top menu of the APIC window, select TENANTS.
	
	b. From the top sub-menu, select **Visa**.
	
	d. Return to the PuTTY window and hit <**Enter**> at the **Hit return to process Citrix_Scripts/1N_CreateLDevVip.xml or press‘s’ and return to skip this script** prompt.
	
	e.Verify the creation of the **ADCCluster1** device cluster.

	a. Still in **TENANTS > Visa**, expand **L4-L7 Services** > **L4-L7 Devices** > **ADCCluster1**, which is empty. 

	b. Return to the PuTTY window and hit <**Enter**> at the **Hit return to process
	c. Expand **ADCCluster1**, which is now populated with the **inside**, **outside**, and **mgmt** Logical Interfaces.
	
12. Create the **Concrete Devices** for the **Visa** tenant as follows:

	a. Return to the PuTTY window and hit <**Enter**> at the Hit return to process **Citrix_Scripts/1N_CreateCDev.xml or press‘s’ and return to skip this script** prompt.
	
	![Figure9](images/Figure9.png)
	
	>NOTE: Wait until the device cluster is in a stable state before proceeding. It may take up to 30 seconds and you may need to click the     icon.
	
13. Create

	a. Still in the **Tenant Visa** directory, expand **Application Profiles**, which is empty.

	c. The **sap** application profile drops into the directory as it is created. Expand **sap > Application EPGs to view the EPGs** - **EPG App** and **EPG Web**.

14. Create the **http** contract as follows:

	a. Expand **Security Policies > Contracts**.
	
	

15. Create the **Webgraph** Service Graph as follows:

	a. Still in the **Tenant Visa** directory, expand **L4-L7 Services > L4-L7 Service Graph Templates**, which is empty.
	


	![Figure10](images/Figure10.png)


16. Optional – Click Function Node – N1 to show the items that have been configured.


![Figure11](images/Figure11.png)
> Note: The next step runs the script that attaches the Service Graph to the Contract. To perform the procedure manually, type **s** at the prompts for the **Citrix_Scripts/1N_AttachWebGraph.xml** script:

19. Attach the **Service Graphs** to the **Visa** tenant, as follows:
![Figure12](images/Figure12.png)

21. Return to the VMWare Client to see that the new port-profiles have been created.
![Figure13](images/Figure13.png)

22. Check the Recent Tasks bar to see the tasks to attach the new port-profiles to the Virtual machine – vpx1.

23. In the Location bar, click **Networking** and select **Hosts and Clusters** from the drop-down.
![Figure15](images/Figure15.png)

24. Click **vpx1** and click the **Summary** tab to display the parameters.
![Figure16](images/Figure16.png)

25. Click **Edit Settings** to bring up the **Parameters** configuration window, open to the **Hardware** tab. This shows the network adapters, relating the APIC EPGs to the Contract.
>NOTE: Check the Do Not Show This Message Again checkbox on the Restricted Virtual Machine Settings pop-up, and click OK. This warning can be ignored.
![Figure17](images/Figure17.png)

26. Return to the APIC and navigate to the **Tenant Visa > L4-L7 Services > Deployed Graph Instances** folder.
![Figure18](images/Figure18.png)

28. Expand Deployed Devices and click **ADCCluster1-Visactx1** to review VLANs.
![Figure19](images/Figure19.png)

29. Verify that the MAC addresses and the correct Port-Profiles show:

	
	
	![Figure20](images/Figure20.png)

30. Open a new **Chrome** tab. In the Chrome Bookmarks Toolbar, click the **Netscaler VPX** bookmark and log in (**nsroot/C1sco12345**).
  ![Figure21](images/Figure21.png)

32. In the side menu, click **Traffic Management > Load Balancing > Virtual Servers** to display the Virtual Server created by the APIC.
  ![Figure22](images/Figure22.png)

33. [Remove the configuration and reset the environment](../Scenario4) prior to starting another scenario.