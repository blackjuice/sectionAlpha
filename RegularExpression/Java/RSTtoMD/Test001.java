public class Test001 {

    private final String re_00 = "====+|----+";         // === || ---
    private final String re_01 = "(\.\.) [a-z]+::";     // .. toctree::
    private final String re_02 = ":[a-z]+:";            // :maxdepth:
    

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

            // store previous line
            String prev_line = in.readLine();
            while (true) {
                // reading current line
                String curr_live = in.readLine();

                // if current line is null, end file and read next file
                if (curr_live == null) break;

                // if ..toctree::
                if ( curr_live.matches(re_00) ) {
                    StdOut.println(prev_line + "\n" + curr_live);
                    StdOut.println("<i>previous filename: " + args[i] + "</i>");
                }

                if ( !curr_live.matches(re_01) && !curr_live.matches(re_02) ) {

                    if (curr_live.equals(".. glossary::")) {
                        curr_live = curr_live.replaceAll(".. glossary::+", "");
                        // previous atttempt with back line:
                        //  StdOut.println("\033[F\033[F\033[F\033[F" + t + "\n"); // \033[F is the back line
                        flag = true;
                        prev_line = prev_line.replaceAll("\t", "");
                        curr_live = curr_live.replaceAll("\t", "");
                        StdOut.println(prev_line + "\n\n" + curr_live);
                    }

                    else {
                        flag = false;
                        prev_line = prev_line.replaceAll("\t", "");
                        curr_live = curr_live.replaceAll("\t", "");
                        //StdOut.println(prev_line + "\n\n" + curr_live);
                        StdOut.println("\n" + curr_live);
                    }
                }
                prev_line = curr_live;
            }
        }

        StdOut.println("\n----\n"); // end of all files


/*
            while (!in.isEmpty()) {
                // read line
                String t = in.readLine();

                // if line contains ====, the next reading line should contain \n
                String re = "====+"; //re is the regular expression
                if (t.matches(re)) System.out.println(line);

                // removing line: .. glossary::
                if (t.equals(".. glossary::")) {
                    t = t.replaceAll(".. glossary::+", "");
                    // previous atttempt with back line:
                    //  StdOut.println("\033[F\033[F\033[F\033[F" + t + "\n"); // \033[F is the back line
                    StdOut.println( t );
                }

                //else if (t.equals("===+\n{4}")) {

                //}

                else {
                    //t = t.replaceAll("\n", "");
                    t = t.replaceAll("\t", "");
                    StdOut.println(t);
                    //StdOut.println(t);
                }
                //String t_new = t.replaceAll(".. glossary::+|   +", "");
                //StdOut.println(t_new);
            }

            StdOut.println("\n\n");
        }
*/
/*
        In in = new In(args[0]);
        EdgeWeightedDigraph G = new EdgeWeightedDigraph(in);
        StdOut.println(G);

        String[] words = StdIn.readAllStrings();

        for (int i = 0; i < words.length; i++) {
            StdOut.println(words[i]);
        }

        //In in = new In(args[0]);
        In in[] = new In(args[0]); 
        String filename  = args[0];
        String delimiter = args[1];
        SymbolEWDigraph sg = new SymbolEWDigraph(filename, delimiter);
        EdgeWeightedDigraph G = sg.G();
        while (!in.isEmpty()) {
            String t = in.readString();
            StdOut.println(t);

            for (int v = 0; v < G.V(); v++) {
                for (DirectedEdge e : G.adj(sg.index(t)) )
                    StdOut.println("   " + sg.name(v));
            }
        }
*/
    }
}
