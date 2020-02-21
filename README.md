# Simple-HTML
This Is A Simple Repository To Create A Simple HTML Page Simpler Than The Main HTML-CSS-JS :)

# Usage
Write Your Simple HTML Code Like That : 
  ```
@html
	@head
		@title Salam ! @@title
	@@head
	
	@style
	#p1{
		color:red;
	}
	@@style
	
	@body(bgcolor=>"black")  <!-- You Are Free To Use '=>' / '->' / ':' / '=' Just You Have To Stick All Of Them ( Dont Use Space ) -->
		@center
			@p|#p1| Test Text It Is ! @@p @br
			@p(style->"color:cyan") Another Test TExt @@p <!-- You Are Free Here Too ! Again, Stick All Of Them(Dont Use Space) -->
		@@center
	@@body
@@html

  ```

Run sht.py File With Your Code Name ! For Example :

`python sht.py code.sht`

Now You Can See Your Page With Name `code.html` !

In Fact Output Is : 

```
<html>
	<head>
		<title> Salam ! </title>
	</head>
	
	<style>
	#p1{
		color:red;
	}
	</style>
	
	<body bgcolor="black">
		<center>
			<p id="p1"> Test Text It Is ! </p> <br>
			<p style="color:cyan"> Another Test TExt </p>
		</center>
	</body>
</html>
```

***

**Important : All Files In Simple HTML Have sht Format**

**Important : Commands Are The HTML Tags But Starting With @ Or @@**

**'@' Means That Tag Started And '@@' Means That Tag Finished**
