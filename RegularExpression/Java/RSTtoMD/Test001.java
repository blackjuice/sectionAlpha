public class Test001 {

    private static String re_00 = "====+|----+";         // === || ---
    private static String re_01 = "(\\.\\.) [a-z]+::";     // .. toctree::
    private static String re_02 = " +:[a-z]+: [1-9]+";            // :maxdepth:
    

    public static void main(String[] args) {

        boolean flag = false;
        /*
            Checking arguments entry quantity
            input:  javac-algs4 Test001.java && java-algs4 Test001 *.rst
            code:
                    if (args.length > 0)
                        StdOut.println("flag**");
        */
        for (int i = 0; i < args.length; i++) {
            In in = new In(args[i]);

            StdOut.println("\n----\n"); // dividing line between one file to another
            StdOut.println("<i>previous filename: " + args[i] + "</i>");
            // store previous line
            String prev_line = in.readLine();
            while (true) {
                // reading current line
                String curr_line = in.readLine();

                // if current line is null, end file and read next file
                if (curr_line == null) break;

                // if ..toctree::
                if ( curr_line.matches(re_00) && !prev_line.equals(curr_line) ) {
                    StdOut.println(prev_line + "\n" + curr_line);
                }

                else if ( !curr_line.matches(re_01) && !curr_line.matches(re_02) ) {
                    StdOut.println(curr_line);
                    //StdOut.println(prev_line + "\n\n" + curr_line);
                }

                prev_line = curr_line;
            }
        }

        StdOut.println("\n----\n"); // end of all files
    }
}
