/*
* 遍历树并输出一个列表，列表中每个元素为树种一条完整的边。
* 输入:
*      a -> b -> c
*      |  |->d
*      |-> e -> f
* 输出:
*      a, b, c
*      a, d
*      a, e, f
* @Author: liuchaozhen
* @Date:   2017-02-20 17:53:41
* @Last Modified by:   liuchaozhen
* @Last Modified time: 2017-02-20 17:56:17
*/
import java.util.*;

public class Test {
    public class IndicatorSimple {
        public List<IndicatorSimple> children = new ArrayList<IndicatorSimple>();
        public String id = "";
    }

    public List<IndicatorSimple> buildIndicator() {
        List<IndicatorSimple> indicatorList = new ArrayList<IndicatorSimple>();
        IndicatorSimple A = new IndicatorSimple();
        A.id = "A";
        IndicatorSimple a1 = new IndicatorSimple();
        a1.id = "a1";
        IndicatorSimple a2 = new IndicatorSimple();
        a2.id = "a2";
        IndicatorSimple a22 = new IndicatorSimple();
        a22.id = "a22";
        IndicatorSimple a221 = new IndicatorSimple();
        a221.id = "a221";
        a22.children.add(a221);
        IndicatorSimple a23 = new IndicatorSimple();
        a23.id = "a23";
        IndicatorSimple a3 = new IndicatorSimple();
        a3.id = "a3";
        a2.children.add(a22);
        a2.children.add(a23);
        A.children.add(a2);
        A.children.add(a1);
        A.children.add(a3);
        indicatorList.add(A);
        IndicatorSimple B = new IndicatorSimple();
        B.id = "B";
        IndicatorSimple b1 = new IndicatorSimple();
        b1.id = "b1";
        IndicatorSimple b11 = new IndicatorSimple();
        b11.id = "b11";
        b1.children.add(b11);
        B.children.add(b1);
        indicatorList.add(B);
        return indicatorList;
    }

    public void calcIndicator(List<IndicatorSimple> lstIndicator, List<List<String>> rows) {
        for (IndicatorSimple indicator : lstIndicator) {
            calcIndicator(indicator, rows);
        }
    }

    public void calcIndicator(IndicatorSimple indicator, List<List<String>> rows) {
        calcIndicator(indicator, rows, null);
    }

    private void calcIndicator(IndicatorSimple indicator, List<List<String>> rows, List<String> path) {
        if (null == rows) {
            return;
        }

        if (null == path) {
            path = new ArrayList<String>();
        }

        if (indicator.children.size() > 0) {
            path.add(indicator.id);
            for (IndicatorSimple iter : indicator.children) {
                List<String> iterPath = new ArrayList<String>();
                iterPath.addAll(path);
                calcIndicator(iter, rows, iterPath);
            }
        } else {
            List<String> row = new ArrayList<String>();
            row.addAll(path);
            row.add(indicator.id);
            rows.add(row);
        }
    }

    public void printIndicators(List<List<String>> rows) {
        for (List<String> row : rows) {
            System.out.println(row);
        }
    }

    public static void main(String[] args) {
        Test app = new Test();
        List<IndicatorSimple> sample = app.buildIndicator();
        List<List<String>> rows = new ArrayList<List<String>>();
        app.calcIndicator(sample, rows);
        app.printIndicators(rows);
    }
}