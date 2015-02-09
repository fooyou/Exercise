
import java.util.HashMap;
import java.util.List;
import java.util.Map.Entry;


public class Serialize {
    /*
     * @Author: Joshua
     * @E-Mail: liuchaozhen@neusoft.com
     * @Date:   2015-02-04 18:20:08
     * @About Serialize.java
     */

    public static void main(String[] args) {
        HashMap<String, HashMap<String, Double>> hm = new HashMap<String, HashMap<String, Double>>();
        HashMap<String, Double> contents = new HashMap<String, Double>();
        contents.put("nr", 1000.0);
        hm.put("照片", contents);
        System.out.println(hm);
    }
}