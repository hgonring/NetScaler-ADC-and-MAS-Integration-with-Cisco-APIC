## Scenario 3. Single Tenant, Single Graph with Multi-Node via Northbound API

> NOTE: If you have already run a scenario that created objects in the APIC, you must [remove those objects](../Scenario4) before running this scenario. 
![Figure 1](images/Figure1.png)
> NOTE: The Python script method calls individual XML scripts to create a series of objects. To pause the script and create an object using an APIC wizard, see the instructions inline. Objects that can be created via wizard using this script are indicated with * in the list below.

The Python script performs the following functions:



*  Verify deployed L4-L7 parameters in NetScaler VPX

![Figure 2](images/Figure2.png)

## Steps

1. From the demonstration workstation, click the **APIC Login** shortcut to open the Application Policy Infrastructure Controller window and log in (**admin/ C1sco12345**).

	![Figure 3](images/Figure3.png)

4. Minimize the ASDM window.

	![Figure 4](images/Figure4.png)

7. Login to PuTTy (**user01/user01**).

	![Figure 5](images/Figure5.png)

9. From the command line type **./request.py Citrix_Scripts/Build_ASA_Citrix.cfg** and hit **<Enter>**.

	> NOTE: To show the XML code as the Python script calls each XML script, substitute

	![Figure 6](images/Figure6.png)

	> This is an example of the partial XML output for the Build_Citrix_VPX.xml script.

	The Build_ASA_Citrix.cfg script utilizes a series of XML scripts to perform the necessary configuration steps. It will pause between each of the XML scripts, and the user can either press <Enter> to run the script, or type s to skip the script and configure the object via a wizard. While the script is running, a brief description will display what that script is doing, while the APIC window updates in real-time. When a script completes successfully, the success code 200 will appear onscreen.

	![Figure 8](images/Figure8.png)

10. Create the **Tenants** 
	
	a. In the APIC top menu, click **Tenants**.
	
	b. Return to the PuTTY window and hit <**Enter**> at the **Hit return to process Citrix_Scripts/2N_Tenant.xmlor press ‘s’ and return to skip this script** prompt. The **Visa** tenant is created and displayed in the window.
	
	![Figure 9](images/Figure9.png)

	d. Expand the **Tenant Visa > Networking > Bridge Domains** directory to show that the **VisaBDApp, VisaBDWeb,
	e. Expand the **Tenant Visa > Networking > VRFs** folder to show that the **Visactx1** private network has been created. 

11. Import the **Citrix NetScaler Device Package** and the **Cisco ASAv Device Package** as follows:

	
	c. Expand the **L4-L7 Services Device Types** folder and show that no packages are present.
	![Figure 10](images/Figure10.png)
	
	> NOTE: The next three steps create the device cluster, concrete devices and logical interfaces in the APIC. To [create these devices manually](../Appendix/Appendix-D), type s and <Enter> at the prompts for the following scripts:

12. Create the **Device Cluster**:
	
	c. Return to the PuTTY window and hit <**Enter**> at the **Hit return to process Citrix_Scripts/2N_CreateLDevVip.xml or press ‘s’ and return to skip this script** prompt.
	
	
13. Export the device cluster as follows:

	
	
14. Create the **Concrete Devices** for the **Visa** tenant as follows:

	
	
	![Figure 11](images/Figure11.png)

	> NOTE: W ait until both devices in the device cluster are in a stable state before proceeding. It may take up to 30 seconds and you may need to click the   icon.

15. Create the Application Profile as follows:
	
	


	![Figure 12](images/Figure12.png)

18. Create the contracts as follows:

	
	c. **webCtrct > http** is created in **Contracts**. 
	
19. Create the WebGraph **Service Graph** as follows:
	
	b. Return to the PuTTY window and hit <**Enter**> at the **Hit return to process

	c. **WebGraph** is created in the **L4-L7 Service Graph Templates** folder, with **Function Node – N1**, and **Function Node

	d. Expand the two **Function Nodes** to show the objects that have been created.
	
	![Figure 13](images/Figure13.png)

20. Optional – Click each **Function Node** to show all the parameters that have been configured.

	> NOTE: The next step runs the script that attaches the Service Graph to the Contract. To [perform the procedure manually](../Appendix/Appendix-E), type **s** at the prompts for the **Citrix_Scripts/2N_AttachGraphToContract.xml** script:



	![Figure 14](images/Figure14.png)

23. Click webCtrct-WebGraph-Visa to see the topology of the deployed Service Graph.

	![Figure 15](images/Figure15.png)

24. Expand Deployed Devices and click ADCCluster1-visactx1 and Firewall-visactx1 to review the VLANs allocated.

	![Figure 15b](images/Figure15b.png)

25. Open a new **Chrome** tab. In the Chrome Bookmarks Toolbar, click the **NetScaler VPX** shortcut and login with credentials **nsroot/C1sco12345**.

	![Figure 16](images/Figure16.png)

27. Expand **System > Network** on the left menu and click **VLANs** to display the VLANs. Verify that the VLANs match the ones from the ADCCluster1 device in APIC.

	![Figure 17](images/Figure17.png)

28. Return to vSphere, or login with **Windows login credentials**.
 

	![Figure 18](images/Figure18.png)

30. In the Location bar, click **Networking** and select **Hosts and Clusters** from the drop-down.

	![Figure 19](images/Figure19.png)

31. Click **vpx1** to display the parameters.

	![Figure 20](images/Figure20.png)

33. Click **network adapter 2** and **network adapter 3** to display the MAC addresses. Use the displayed MAC addresses to compare them to those in the APIC (see Step 33).

	![Figure 21](images/Figure21.png)

34. Verify that the MAC addresses and PORTGROUP show in the **APIC** window:

		
	
	![Figure 22](images/Figure22.png)

35. If desired, repeat Steps 31-34, this time clicking **ASAv** in vSphere and APIC to compare the MAC addresses.

	![Figure 23](images/Figure23.png)

38. [Remove the configuration and reset the environment](../Scenario4) prior to starting another scenario.