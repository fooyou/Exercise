package com.neusoft;

import java.io.*;
import org.ansj.domain.Term;
import org.ansj.splitWord.Analysis;
import org.ansj.splitWord.analysis.ToAnalysis;

/**
 * Hello world!
 *
 */
public class WordSplit {
    public static void main(String[] args) throws IOException {
        String input = "";
        String output = "output.txt";
        if (args.length >= 1) {
            input = args[0];
            System.out.println(input);
            if (args.length > 1) {
                output = args[1];
            }
        }
        
        try {
            FileOutputStream fos = new FileOutputStream(new File(output));
            try {
                String encoding = "utf-8";
                File file = new File(input);
                if (file.isFile() && file.exists()) { //判断文件是否存在
                    InputStreamReader read = new InputStreamReader(
                    new FileInputStream(file), encoding);//考虑到编码格式
                    BufferedReader bufferedReader = new BufferedReader(read);
                    String lineTxt = null;
                    while ((lineTxt = bufferedReader.readLine()) != null) {
                        System.out.println(lineTxt);
                    }
                    read.close();
                }else{
                    System.out.println("找不到指定的文件");
                }
            } catch (Exception e) {
                System.out.println("读取文件内容出错");
                e.printStackTrace();
            }

            fos.close();
        }
        catch (Exception e) {
            e.printStackTrace();
        }

        Analysis udf = new ToAnalysis(new StringReader("地铁"));
        Term term = null;
        while ((term=udf.next()) != null) {
            System.out.print(term.getName()+"\n");
        }
    }
}
