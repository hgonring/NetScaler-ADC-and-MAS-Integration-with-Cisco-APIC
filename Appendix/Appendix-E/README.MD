# Appendix E. Attach Service Graphs to Tenants

> **NOTE**: This step replaces Steps 22 and 23 in [Scenario 2](../../Scenario2), or Step 27 in [Scenario 3](../../Scenario3).
>
  * If you are performing [Scenario 2](../../Scenario2), type **s** and **< Enter >** for the `Citrix_Scripts/AttachWebGraph.xml` script.
  *  If you are performing [Scenario 3](../../Scenario3), type **s** and **< Enter >** for the `ASA_Citrix_Script/AttachWebGraph.xml`  script.

Use this procedure to attach a Service Graph to a Tenant. If there a multiple tenants or multiple service graphs in a scenario, the procedure must be repeated for each graph for each tenant.

## Steps 

1. In the APIC window, select **TENANTS** from the top menu.

2. Select the **Visa** tenant from the top sub-menu.

3. Expand the **L4-L7 Services > Deployed Service Graphs** hierarchy, which is empty.

4. Expand the **Security Policies > Contracts > webContract** hierarchy and click **http.**

5. From the **Service Graph** drop-down, select the name of the service graph that you are attaching to this tenant.

6. Click **Submit**. The selected service graph now appears in the **L4-L7 Services > Deployed Service Graphs** folder.
  
  ![Tennant Service Graph](images/Tennant-Service-Graph.png)

7. Return to the appropriate scenario:

  * If you are performing Scenario 2, [click here](../../Scenario2) to verify that the graphs are attached.
  * If you are performing Scenario 3, [click here](../../Scenario3) to verify that the graphs are attached.
