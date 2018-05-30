<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="17008000">
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="Helpers" Type="Folder" URL="../Helpers">
			<Property Name="NI.DISK" Type="Bool">true</Property>
		</Item>
		<Item Name="Gains.ctl" Type="VI" URL="../Gains.ctl"/>
		<Item Name="Plant.ctl" Type="VI" URL="../Plant.ctl"/>
		<Item Name="PlantUpdate.vi" Type="VI" URL="../PlantUpdate.vi"/>
		<Item Name="StateSpaceController.vi" Type="VI" URL="../StateSpaceController.vi"/>
		<Item Name="StateSpaceObserver.vi" Type="VI" URL="../StateSpaceObserver.vi"/>
		<Item Name="StateSpaceTest.vi" Type="VI" URL="../StateSpaceTest.vi"/>
		<Item Name="TrapezoidalMotionProfile.vi" Type="VI" URL="../TrapezoidalMotionProfile.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="NI_AALBase.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALBase.lvlib"/>
				<Item Name="NI_AALPro.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/NI_AALPro.lvlib"/>
				<Item Name="NI_Matrix.lvlib" Type="Library" URL="/&lt;vilib&gt;/Analysis/Matrix/NI_Matrix.lvlib"/>
			</Item>
			<Item Name="lvanlys.dll" Type="Document" URL="/&lt;resource&gt;/lvanlys.dll"/>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
