<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>SFTools</class>
 <widget class="QMainWindow" name="SFTools">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>619</width>
    <height>738</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="windowTitle">
   <string>SFTools</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QHBoxLayout" name="horizontalLayout">
    <property name="spacing">
     <number>6</number>
    </property>
    <property name="leftMargin">
     <number>0</number>
    </property>
    <property name="topMargin">
     <number>9</number>
    </property>
    <property name="rightMargin">
     <number>0</number>
    </property>
    <property name="bottomMargin">
     <number>0</number>
    </property>
    <item>
     <widget class="QTabWidget" name="fixWin10">
      <property name="enabled">
       <bool>true</bool>
      </property>
      <property name="currentIndex">
       <number>0</number>
      </property>
      <widget class="QWidget" name="tabyt2mp3">
       <attribute name="title">
        <string>Youtube to MP3</string>
       </attribute>
       <widget class="QPushButton" name="pBBajarVideo">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>150</y>
          <width>91</width>
          <height>23</height>
         </rect>
        </property>
        <property name="text">
         <string>Download</string>
        </property>
       </widget>
       <widget class="QPushButton" name="pBPlaylistBajar">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>300</y>
          <width>91</width>
          <height>23</height>
         </rect>
        </property>
        <property name="text">
         <string>Download</string>
        </property>
       </widget>
       <widget class="QLabel" name="lVideos">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>10</y>
          <width>591</width>
          <height>41</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>true</bool>
        </property>
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;WARNING: Videos and playlists must be hidden or public, private videos are not findable by the app browser so using them will result on an URL error&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
        <property name="wordWrap">
         <bool>true</bool>
        </property>
       </widget>
       <widget class="QLabel" name="lPlaylists">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>220</y>
          <width>321</width>
          <height>17</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Download a Full playlist&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
       </widget>
       <widget class="QTextEdit" name="tEVideoBajar">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>110</y>
          <width>191</width>
          <height>31</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <weight>50</weight>
          <bold>false</bold>
         </font>
        </property>
        <property name="html">
         <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; color:#6a6a6a;&quot;&gt;Introduce video URL&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
       </widget>
       <widget class="QTextEdit" name="tEPlaylistBajar">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>260</y>
          <width>191</width>
          <height>31</height>
         </rect>
        </property>
        <property name="html">
         <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; color:#6a6a6a;&quot;&gt;Introduce playlist URL&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
       </widget>
       <widget class="QLabel" name="lVideos_2">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>70</y>
          <width>321</width>
          <height>17</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>Download a Single Video:</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
       </widget>
       <widget class="QPlainTextEdit" name="pTEStatus">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>390</y>
          <width>591</width>
          <height>271</height>
         </rect>
        </property>
        <property name="readOnly">
         <bool>true</bool>
        </property>
       </widget>
       <widget class="QLabel" name="lPlaylists_3">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>360</y>
          <width>321</width>
          <height>17</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Status:&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
       </widget>
      </widget>
      <widget class="QWidget" name="tabForceDelete">
       <property name="enabled">
        <bool>false</bool>
       </property>
       <attribute name="title">
        <string>Force Deletion</string>
       </attribute>
       <widget class="QLabel" name="lArchivos">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>10</y>
          <width>321</width>
          <height>17</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>Files:</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
       </widget>
       <widget class="QLineEdit" name="lEArchivoBorrar">
        <property name="enabled">
         <bool>false</bool>
        </property>
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>50</y>
          <width>161</width>
          <height>21</height>
         </rect>
        </property>
        <property name="focusPolicy">
         <enum>Qt::NoFocus</enum>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="readOnly">
         <bool>true</bool>
        </property>
       </widget>
       <widget class="QPushButton" name="pBSeleccionarArchivoBorrar">
        <property name="geometry">
         <rect>
          <x>180</x>
          <y>50</y>
          <width>75</width>
          <height>23</height>
         </rect>
        </property>
        <property name="text">
         <string>Find..</string>
        </property>
       </widget>
       <widget class="QPushButton" name="pBForzarBorradoArchivo">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>90</y>
          <width>91</width>
          <height>23</height>
         </rect>
        </property>
        <property name="text">
         <string>Force delete</string>
        </property>
       </widget>
       <widget class="QPushButton" name="pBForzarBorradoCarpeta">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>240</y>
          <width>91</width>
          <height>23</height>
         </rect>
        </property>
        <property name="text">
         <string>Force delete</string>
        </property>
       </widget>
       <widget class="QLabel" name="lCarpetas">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>160</y>
          <width>321</width>
          <height>17</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>Folders:</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
       </widget>
       <widget class="QLineEdit" name="lECarpetaBorrar">
        <property name="enabled">
         <bool>false</bool>
        </property>
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>200</y>
          <width>161</width>
          <height>21</height>
         </rect>
        </property>
        <property name="focusPolicy">
         <enum>Qt::NoFocus</enum>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="readOnly">
         <bool>true</bool>
        </property>
       </widget>
       <widget class="QPushButton" name="pBSeleccionarCarpetaBorrar">
        <property name="geometry">
         <rect>
          <x>180</x>
          <y>200</y>
          <width>75</width>
          <height>23</height>
         </rect>
        </property>
        <property name="text">
         <string>Find..</string>
        </property>
       </widget>
      </widget>
      <widget class="QWidget" name="tabFixes">
       <property name="enabled">
        <bool>false</bool>
       </property>
       <attribute name="title">
        <string>Fixes</string>
       </attribute>
       <widget class="QPushButton" name="pBResetExplorer">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>50</y>
          <width>91</width>
          <height>23</height>
         </rect>
        </property>
        <property name="text">
         <string>Fix explorer</string>
        </property>
       </widget>
       <widget class="QLabel" name="lResetExplorer">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>10</y>
          <width>321</width>
          <height>17</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>Fix explorer for resolving navigation bugs</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
       </widget>
      </widget>
      <widget class="QWidget" name="tabDCBind">
       <property name="enabled">
        <bool>false</bool>
       </property>
       <attribute name="title">
        <string>Disconnect Bind</string>
       </attribute>
       <widget class="QLabel" name="lPlaylists_2">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>160</y>
          <width>321</width>
          <height>17</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Set Bind (click in the box and press key combination):&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
       </widget>
       <widget class="QLabel" name="lVideos_3">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>10</y>
          <width>591</width>
          <height>41</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Disconnect bind allows you to bind the instant disconnect from the internet for any applicatión you choose within the settings on this tab&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
        <property name="wordWrap">
         <bool>true</bool>
        </property>
       </widget>
       <widget class="QLabel" name="lVideos_4">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>70</y>
          <width>321</width>
          <height>17</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>Choose what application will get closed</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
       </widget>
       <widget class="QTextEdit" name="tEPlaylistBajar_2">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>200</y>
          <width>191</width>
          <height>31</height>
         </rect>
        </property>
       </widget>
       <widget class="QPushButton" name="pBPlaylistBajar_2">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>240</y>
          <width>91</width>
          <height>23</height>
         </rect>
        </property>
        <property name="text">
         <string>Add</string>
        </property>
       </widget>
       <widget class="QPushButton" name="pBSeleccionarArchivoBorrar_2">
        <property name="geometry">
         <rect>
          <x>180</x>
          <y>110</y>
          <width>75</width>
          <height>23</height>
         </rect>
        </property>
        <property name="text">
         <string>Find..</string>
        </property>
       </widget>
       <widget class="QLineEdit" name="lEArchivoBorrar_2">
        <property name="enabled">
         <bool>false</bool>
        </property>
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>110</y>
          <width>161</width>
          <height>21</height>
         </rect>
        </property>
        <property name="focusPolicy">
         <enum>Qt::NoFocus</enum>
        </property>
        <property name="text">
         <string/>
        </property>
        <property name="readOnly">
         <bool>true</bool>
        </property>
       </widget>
       <widget class="QTableView" name="tablaBindings">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>370</y>
          <width>591</width>
          <height>301</height>
         </rect>
        </property>
        <property name="gridStyle">
         <enum>Qt::DashLine</enum>
        </property>
       </widget>
       <widget class="QLabel" name="lPlaylists_4">
        <property name="geometry">
         <rect>
          <x>10</x>
          <y>340</y>
          <width>321</width>
          <height>17</height>
         </rect>
        </property>
        <property name="font">
         <font>
          <family>Segoe UI</family>
          <pointsize>10</pointsize>
          <weight>75</weight>
          <bold>true</bold>
         </font>
        </property>
        <property name="autoFillBackground">
         <bool>false</bool>
        </property>
        <property name="text">
         <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;Binds:&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
        </property>
        <property name="alignment">
         <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
        </property>
       </widget>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="enabled">
    <bool>true</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>619</width>
     <height>18</height>
    </rect>
   </property>
   <property name="nativeMenuBar">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
