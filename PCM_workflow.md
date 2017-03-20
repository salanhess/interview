# Normal workflow(Include scrum/Agile/DevOps) #
>refer to [在复杂的网络环境下构建 DevOps 测试的最佳实践](https://www.ibm.com/developerworks/cn/devops/1608_baik_test/index.html)

## Worksteps ##
![Wholeworkflow](https://www.ibm.com/developerworks/cn/devops/1608_baik_test/image008.png)

> + [Test Coverage Strategy] Design test scope
> + [Test Coverage Strategy] Adjust test scope and resource in-time
> + [Test Coverage Strategy] Optimize automation cases and scripts 
> + [Behavior-Driven Development] Convert Customer's new requirement into user story
> + [Behavior-Driven Development] Publish online document based on early build 
> + [Test Environment Management] Scripted and scheduled test server 
> + [Function test automation] Convert fixed issues/new feature into automation cases 
> + [Function test automation] Execute daily automation and generate report 
> + [Continuous Testing] Embedding Test into Continuous Integration 


### Design test scope ###
According to FS(Functional Requirement Specification)
> * . FUNCTIONAL REQUIREMENTS
> * . FUNCTIONAL DESCRIPTIONS
> * . USE CASE

### Optimize automation cases and scripts ###
A 7x24 test with following schedule: 
> * . Manually testing from 9:00 am to 18:00 pm
> * . Automation smoke test through night
> * . Full scope module automation test at weekend

### Scripted and scheduled test server ###
Based on Testgrid wrapped with Selenium[sə'liniəm] 
> * . Use Java language simple format
> * . use Shell.cmd to send command to shell
> * . Wrapped normal operations such as logon/gotoComWidgetTreeNode in GUI normal Action class
> * . Wrapped normal shell operations such as reboot  in normal Action class
> * . Use Java standard format Assert to check result(Such as Assert.isEqual  / Assert.findKeywords /Assert.isNull etc)
> * . Define group /priority /keyword at the head of each case, easy to group and call together
> * . Configuration Cluster ManageNode/ComputeNode via xml format, easy to call suite scripts for different environment

    testscript
    desc="add/remove kit"
    author="carol"
    group="pcm_gui"
    priority=P1
    keyword=regression, OS_porting
    features=OS_porting_Image_Profile,Provision
    CN1_CECNAME = PCMAction.getCNCEC(CN1_NAME);
    //set firefox run module. FIREFOX_IDE/FIREFOX_GUI 
    BrowserFactory.FIREFOX_MODULE = BrowserFactory.FIREFOX_GUI;
    BrowserFactory  Factory = BrowserFactory.getInstance("localhost", SE.CASE_SHARED_DIR());
    date = Shell.cmd("pty date +%m%d").get(0);
    Window br = Factory.create();
    br.navigate("http://" + WEBGUI_IP);
    PCMGUIAction.setBrowserObject(br);
    PCMGUIAction.logon(WEBGUI_USERID, WEBGUI_PASSWORD);
    result_message = PCMGUIAction.getGUIMessage("modified");
    Assert.findKeywords(result_message, "modified.");
    //Set string and verify
    alert_filter_hm= new HashMap<String, String>();
    alert_filter_hm.put("Name", alert_name);
    PCMGUIAction.setAlertFilter(alert_filter_hm);
    real_alertPolicy_name=PCMGUIAction.getAlertPolicy(alert_name).getCell("Name").innerText();
    Assert.isEqual(alert_name, real_alertPolicy_name, "Assert failed.");
    //Set ArrayList and verify
    ArrayList<String> userGroup = new ArrayList<String>();
    ArrayList<String> userNameAA = new ArrayList<String>();
    userGroup.add(USER_GROUP1);
    userGroup.add(USER_GROUP2);
    userNameAA.add(USER_NAME_AA1);
    userNameAA.add(USER_NAME_AA2);
    HashMap<String, ArrayList<String>> userInfo = new HashMap<String, ArrayList<String>>();
    userInfo.put( "userGroup", userGroup);
    userInfo.put( "userNameAA", userNameAA);
    PCMGUIAction.createClusterAccount(accountInfo,userInfo);
    return_msg=PCMGUIAction.getGUIMessage("Account");
    Assert.findKeywords(return_msg, "Account added");
    

    

