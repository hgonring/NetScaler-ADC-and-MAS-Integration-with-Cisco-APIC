## Scenario 4. Removing APIC Objects

This scenario can only be performed after the APIC objects are created, whether the creation method was via Python script, APIC wizard, or manual.

>**NOTE**: If performing this Scenario immediately after Scenario 2, leave the APIC window open with all the directories expanded, to demonstrate the objects being removed in real-time.

fancy_lists

1. If the PuTTY application is closed and you have to reopen it, it will be necessary to reload the Python script package, as follows:
 
	1. From the demonstration workstation, launch **PuTTY**.
	2. In the **PuTTY** **Configuration** window:

		1. In the **Saved Sessions** area, double-click **TOOLS**.
		2. Log in with the following credentials: Username: **user01**, Password: **user01**.

 > The python script will step through multiple XML scripts to remove the objects. Display the APIC window, open to Tenants > Visa, expanding each folder to see the objects being removed.

3. Press **ENTER** at each prompt to walk through the script.

 ![Screenshot1](images/Screenshot1.png)

 ![Screenshot2](images/Screenshot2.png)

4. Close all open application windows, returning to the wkst1 desktop.

