public class Test001 {

    private static String re_00 = "===+|---+|\\*\\*\\*+";              // === || ---
    private static String re_01 = "(\\.\\.) \\w+::";      // .. toctree::
//  private static String re_02 = " +:[a-z]+: [1-9]+";    // :maxdepth:
    private static String re_02 = " +:\\w+:\\s\\w";            // :maxdepth:
    private static String re_03 = "\\* \\w+|\\!|\\;|\\.|\\?";              // "* text"
    private static String re_04 = "`|\\>`\\_"; // removing `info <www.link.com/>`_
    

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
            String curr_line = in.readLine();
            //StdOut.println(curr_line); // printing Title
            while (true) {
                // reading current line
                String next_line = in.readLine();
                // if current line is null, end file and read next file
                if (next_line == null) {
                    curr_line = curr_line.replaceAll("\t|   +", ""); // replace tabs
                    //StdOut.println("curr > " + curr_line + "\n");
                    StdOut.println(curr_line + "\n");
                    break;
                }

                // if === or ----
                if ( next_line.matches(re_00)) {
                    //StdOut.println( next_line );
                    StdOut.println( curr_line + "\n" + next_line );
                    //StdOut.println("** " + next_line);
                }

                //else if (  curr_line.matches(re_00) ) {
                //    StdOut.println("** " + curr_line);
                //}
                // if != ..toctree:: or :maxdepth:
                //else if ( !next_line.matches(re_01) && !next_line.matches(re_02) && !next_line.matches(re_00) ) {
                else if ( !curr_line.matches(re_01) && !curr_line.matches(re_02) && !curr_line.matches(re_00) ) {
                    //next_line = next_line.replaceAll("\t|   +", ""); // replace tabs
                    //StdOut.println("curr > " + next_line + "\n");
                    curr_line = curr_line.replaceAll("\t|   +", ""); // replace tabs
                    curr_line = curr_line.replaceAll(re_04, ""); // replace tabs
                    //StdOut.println("curr > " + curr_line + "\n");
                    if ( !curr_line.matches(re_03) ) {
                        //curr_line = curr_line.replaceAll("\t|   +", ""); // replace tabs
                        //StdOut.println("* " + curr_line + "\n");
                        StdOut.println(curr_line + "\n");
                    }
                }

                curr_line = next_line;
            }
        }

        StdOut.println("\n----\n"); // end of all files
    }
}
