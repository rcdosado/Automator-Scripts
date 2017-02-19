// A Hello World! program in C#.
using System;
using System.Runtime.InteropServices;
using System.Collections.Generic;
using System.Diagnostics;

using System.Reflection;
using System.Text;
using System.Text.RegularExpressions;

namespace Princesa
{

	public class WindowHandleInfo
	{
		private delegate bool EnumWindowProc(IntPtr hwnd, IntPtr lParam);

		[DllImport("user32")]
		[return: MarshalAs(UnmanagedType.Bool)]
		private static extern bool EnumChildWindows(IntPtr window, EnumWindowProc callback, IntPtr lParam);

		private IntPtr _MainHandle;

		public WindowHandleInfo(IntPtr handle)
		{
			this._MainHandle = handle;
		}

		public List<IntPtr> GetAllChildHandles()
		{
			List<IntPtr> childHandles = new List<IntPtr>();

			GCHandle gcChildhandlesList = GCHandle.Alloc(childHandles);
			IntPtr pointerChildHandlesList = GCHandle.ToIntPtr(gcChildhandlesList);

			try
			{
				EnumWindowProc childProc = new EnumWindowProc(EnumWindow);
				EnumChildWindows(this._MainHandle, childProc, pointerChildHandlesList);
			}
			finally
			{
				gcChildhandlesList.Free();
			}

			return childHandles;
		}

		private bool EnumWindow(IntPtr hWnd, IntPtr lParam)
		{
			GCHandle gcChildhandlesList = GCHandle.FromIntPtr(lParam);

			if (gcChildhandlesList == null || gcChildhandlesList.Target == null)
			{
				return false;
			}

			List<IntPtr> childHandles = gcChildhandlesList.Target as List<IntPtr>;
			childHandles.Add(hWnd);

			return true;
		}
	}

    class Hello 
    {
		[DllImport("user32.dll", EntryPoint = "FindWindowEx")]
		public static extern IntPtr FindWindowEx(IntPtr hwndParent, IntPtr hwndChildAfter, string lpszClass, string lpszWindow);
		
		[DllImport("user32.dll", EntryPoint = "SendMessage", CharSet = System.Runtime.InteropServices.CharSet.Auto)]         
		public static extern bool SendMessage(IntPtr hWnd, uint Msg, int wParam, StringBuilder lParam);

		[DllImport("user32.dll", SetLastError = true)]
        public static extern IntPtr SendMessage(int hWnd, int Msg, int wparam, int lparam);

        const int  WM_GETTEXT = 0x000D;
        const int  WM_GETTEXTLENGTH = 0x000E;

		

        static void Main() 
        {
			Process[] anotherApps = Process.GetProcessesByName("Foxit Reader");
			if (anotherApps.Length == 0) return;


			// Register Key


			if (anotherApps[0] != null)
			{
				var allChildWindows = new WindowHandleInfo(anotherApps[0].MainWindowHandle).GetAllChildHandles();
				
				// find the page number
				string pattern = @"^(\d{1,5}\s/\s\d{1,5})";
				Regex rgx = new Regex(pattern, RegexOptions.IgnoreCase);


				foreach(var item in allChildWindows)
				{	
					StringBuilder title = new StringBuilder();

					// Get the size of the string required to hold the window title. 
					Int32 size = SendMessage((int)item, WM_GETTEXTLENGTH, 0, 0).ToInt32();

					if( size > 0){
						title = new StringBuilder(size + 1);
						SendMessage(item, (int) WM_GETTEXT, title.Capacity, title);
					}
					MatchCollection matches = rgx.Matches(title.ToString());
					if(matches.Count>0){
						string[] raw = title.ToString().Split(' ');
						Console.WriteLine("Current Page:"+raw[0]+" Total:"+raw[2]);						
					}
					else
						Console.WriteLine(title.ToString());
				}
			}
        }
    }
}