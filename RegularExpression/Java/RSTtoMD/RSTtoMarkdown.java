/*
    author: Lucas Sung Jun Hong (github user: blackjuice)

    This program converts personal .rst files to a single .md file using regular expressions:
    * converting link texts to .md readable format;
    * anchoring titles;
    * removing unnecessary tabs, spaces;

    references:
    * http://regexr.com
    
    Little personal reference:
        Checking arguments entry quantity
        input:  javac-algs4 Test001.java && java-algs4 Test001 *.rst
        code:
                if (args.length > 0)
                    StdOut.println("flag**");

    Compilation and execution time (90 files in total):
    1.91s user
    0.12s system
    213% cpu
    0.949 total
*/

public class RSTtoMarkdown {

    private static String re_00 = "===+|---+|\\*\\*\\*+";           // === || ---
    private static String re_01 = "(\\.\\.) \\w+::";                // .. toctree::
    private static String re_02 = "( +:\\w+:\\s\\w)|( +:\\w+:)";    // :maxdepth: = " +:\\w+:\\s\\w"; " +:[a-z]+: [1-9]+";
    //private static String re_03 = "\\* \\w+|\\!|\\;|\\.|\\?";     // "* text"
    //private static String re_04 = "`|\\>`\\_";                    // removing `info <www.link.com/>`_
    private static String re_05 = "\t|   +|`|\\>`\\_";              // re_04 + tabs
    

    public static void main(String[] args) {

        boolean     flag = false;
        String      filename;

        for (int i = 0; i < args.length; i++) {
            In in = new In(args[i]);

            // custom convertion for index
            if (args[i].equals("index.rst")) {
                // dividing line between one file to another
                StdOut.println("\n----\n");
                filename                = args[i].replaceAll("(.rst)", ""); // replace link:
                StdOut.println( "<a name=\"" + filename + "\"></a>" + "previous filename: " + args[i] );
                String curr_line        = in.readLine(); // store current line

                while (true) {
                    String next_line    = in.readLine(); // reading next_line
                    // if current line is null, print last line and end file and read next file
                    if (next_line == null) {
                        curr_line       = curr_line.replaceAll(re_05, " "); // replace tabs
                        curr_line       = curr_line.replaceAll("\\<", ":"); // replace link:

                        StdOut.println(curr_line + "\n");
                        break;
                    }

                    // if === or ---- (creates anchor name)
                    if ( next_line.matches(re_00))
                        StdOut.println( "\n" + curr_line + "\n" + next_line + "\n" );

                    // if list
                    else if (   !curr_line.matches(re_01) && 
                                !curr_line.matches(re_02) && 
                                !curr_line.matches(re_00) ) {

                        curr_line       = curr_line.replaceAll(re_05, ""); // replace tabs
                        curr_line       = curr_line.replaceAll("\\<", ":"); // replace link:

                        if ( !curr_line.equals("") ) // if not a blank
                            StdOut.println( "* " + "["+ curr_line + "](#" + curr_line + ")" );
                    }
                    curr_line = next_line; // next_line becomes present_line
                }
            }

            // custom convertion for database
            else if (args[i].equals("database.rst")) {
                // dividing line between one file to another
                StdOut.println("\n----\n");
                filename                = args[i].replaceAll("(.rst)", ""); // replace link:
                StdOut.println( "<a name=\"" + filename + "\"></a>" + "previous filename: " + args[i] );
                //StdOut.println("<i>previous filename: " + "["+ args[i] + "](#" + args[i] + ")" + "</i>");

                String curr_line        = in.readLine(); // store current line

                while (true) {
                    String next_line    = in.readLine(); // reading next_line
                    // if current line is null, print last line and end file and read next file
                    if (next_line == null) {
                        curr_line       = curr_line.replaceAll(re_05, " "); // replace tabs
                        curr_line       = curr_line.replaceAll("\\<", ":"); // replace link:

                        StdOut.println(curr_line + "\n");
                        break;
                    }

                    // if === or ---- (creates anchor name)
                    if ( next_line.matches(re_00)) {
                        // Main title is anchor
                        //if ( next_line.matches("===+") )
                            //StdOut.println( "<a name=\"" + curr_line + "\"></a>" + curr_line + "\n" + next_line + "\n" );
                            StdOut.println( "\n" + curr_line + "\n" + next_line + "\n" );
                        //else
                            //StdOut.println( "\n" + curr_line + "\n" + next_line + "\n" );
                    }

                    // if list
                    else if (   !curr_line.matches(re_01) && 
                                !curr_line.matches(re_02) && 
                                !curr_line.matches(re_00) ) {

                        curr_line       = curr_line.replaceAll(re_05, ""); // replace tabs
                        curr_line       = curr_line.replaceAll("\\<", ":"); // replace link:

                        if ( !curr_line.equals("") ) // if not a blank
                            StdOut.println( "* " + "["+ curr_line + "](#" + curr_line + ")" );
                    }
                    curr_line = next_line; // next_line becomes present_line
                }
            }

            // default convertion
            else {
                StdOut.println("\n----\n");
                filename                = args[i].replaceAll("(.rst)", ""); // replace link:
                StdOut.println( "<a name=\"" + filename + "\"></a>" + "previous filename: " + args[i] );

                String curr_line        = in.readLine(); // store current line

                while (true) {
                    String next_line    = in.readLine(); // reading next_line
                    // if current line is null, end file and read next file
                    if (next_line == null) {
                        curr_line       = curr_line.replaceAll(re_05, " "); // replace tabs
                        curr_line       = curr_line.replaceAll("\\<", ":"); // replace link:

                        StdOut.println(curr_line + "\n");
                        break;
                    }

                    // if === or ---- 
                    if ( next_line.matches(re_00))
                        StdOut.println( "\n" + curr_line + "\n" + next_line + "\n" );

                    else if (   !curr_line.matches(re_01) && 
                                !curr_line.matches(re_02) && 
                                !curr_line.matches(re_00) ) {

                        curr_line       = curr_line.replaceAll(re_05, " "); // replace tabs
                        curr_line       = curr_line.replaceAll("\\<", ": "); // replace link:

                        if ( !curr_line.equals("") ) // if not a blank
                            StdOut.println(curr_line + "\n");
                    }
                    curr_line = next_line; // next_line becomes present_line
                }
            }
            StdOut.println("\n[⇪ back to top](#index)↳ go to database](#database)\n"); // end of every files
        }
        StdOut.println("\n----\n"); // end of all files
    }
}
