import com.iustu.android.Task;
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;


public class sync
{
	ExecutorService executorService = Executors.newCachedThreadPool();
	public static void main (String[] args)
	{
    	new sync().Tasks();
	}

    private void Tasks()
    {
    	Future<Integer> future1 = executorService.submit(new Callable<Integer>()
    	{
    		public Integer call()
    		{
    			try
    			{
    				int num = Task.taskA();
//    				System.out.println(num);
    				return num;

    			}
    			catch (InterruptedException e)
    			{
    				e.printStackTrace();
    			}
				return null;
    		}
    	});

    	Future<Integer> future2 = executorService.submit(new Callable<Integer>()
    	{
    		public Integer call()
    		{
    			try
    			{
    				int num = Task.taskB();
//    				System.out.println(num);
    				return num;

    			}
    			catch (InterruptedException e)
    			{
    				e.printStackTrace();
    			}
				return null;
    		}
    	});

    	while (true)
    	{
            if (future1.isDone() && future2.isDone())
            {
                try
                {
                    System.out.println(String.format("%d", future1.get() + future2.get()));
                }
                catch (InterruptedException e)
                {
                	System.out.println("error");
                }
                catch (ExecutionException e)
                {
                	System.out.println("error");
                }
                System.exit(0);
            }
            else
            {

            }
        }
    }




}




// package com.iustu.android;
//
// public class Task
// {
//   private Task()
//   {
//     throw new RuntimeException("no instance");
//   }
//
//   public static int taskA()
//     throws InterruptedException
//   {
//     int i = (int)(2.0D + Math.random() * 8.0D);
//     Thread.sleep(1000 * i);
//     return i;
//   }
//
//   public static int taskB()
//     throws InterruptedException
//   {
//     int i = (int)(4.0D + Math.random() * 6.0D);
//     Thread.sleep(1000 * i);
//     return i;
//   }
// }
