package neu.autoclassify;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.apache.lucene.document.Document;
import org.apache.lucene.index.AtomicReader;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.index.SlowCompositeReaderWrapper;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;


// field of doc:
//  <field name="url" type="string" indexed="true" stored="true" required="true" multiValued="false" />
//  <field name="category" type="string" indexed="true" stored="true" required="true" multiValued="false" />
//  <field name="title" type="text_ansj" indexed="true" stored="true" multiValued="false" />
//  <field name="content" type="text_ansj" indexed="true" stored="true" multiValued="true" />
//  <field name="published" type="string" indexed="true" stored="true" />

// public class App 
// {
//     public static void main( String[] args )
//     {
//         System.out.println( "Hello World!" );
//     }
// }

public class App {
    public static String INDEX = "/opt/apache/solr/example/solr/autoclassify/data/index";
    public static final String[] CATEGORIES = {
     "政治",
     "财经",
     "军事",
     "体育",
     "娱乐",
     "科技",
     "社会"
    };
    
    private static int[][] counts;
    private static Map<String, Integer> categoryIndex;
    private static DocAnalyzer docAnalyzer = null;
    
    public static void main(String[] args) throws Exception {
        if (null != args[0] && args[0].length() > 0) {
            INDEX = args[0];
        }
        init();

        final long startTime = System.currentTimeMillis();

        docAnalyzer = new DocAnalyzer(INDEX, "content", "category");

        IndexReader reader = DirectoryReader.open(directory());
        AtomicReader atomicReader = SlowCompositeReaderWrapper.wrap(reader);

        final int maxdoc = reader.maxDoc();
        for (int i = 0; i < maxdoc; i++) {
            System.out.printf("total = %d, cur = %d\n", maxdoc, i);
            Document doc = atomicReader.document(i);
            String correctAnswer = doc.get("category");
            final int cai = idx(correctAnswer);
            String classified = docAnalyzer.Analyze(doc.get("content"));

            if (!classified.equals(correctAnswer)) {
             System.out.printf("Doc(Title: %s, url: %s) unmatch\n", doc.get("title"), doc.get("url"));
            }

            final int cli = idx(classified);
            counts[cai][cli]++;
        }
        
        final long endTime = System.currentTimeMillis();
        final int elapse = (int)(endTime - startTime) / 1000;

        // print results
        printResults();

        System.out.printf("Time = %d (sec); %d docs\n", elapse, maxdoc);
        reader.close();
    }
    
    static void printResults() {
        int fc = 0, tc = 0;
        for (int i = 0; i < CATEGORIES.length; i++) {
            for (int j = 0; j < CATEGORIES.length; j++) {
                System.out.printf(" %3d ", counts[i][j]);
                if (i == j) {
                    tc += counts[i][j];
                }
                else {
                    fc += counts[i][j];
                }
            }
            System.out.println();
        }
        
        float accrate = (float)tc / (float)(tc + fc);
        float errrate = (float)fc / (float)(tc + fc);
        System.out.printf("\n\nAccuracy rate = %f, Error rate = %f;\n", accrate, errrate);
    }
    
    static void init() {
        counts = new int[CATEGORIES.length][CATEGORIES.length];
        categoryIndex = new HashMap<String, Integer>();
        for (int i = 0; i < CATEGORIES.length; i++) {
            categoryIndex.put(CATEGORIES[i], i);
        }
    }
    
    static int idx(String category) {
        return categoryIndex.get(category);
    }
    
    static Directory directory() throws IOException {
        return FSDirectory.open(new File(INDEX));
    }
}