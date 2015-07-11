public class ReadingOrder {

    public static void main(String[] args) {

        for (int i = 0; i < args.length; i++) {
            In in = new In(args[i]);

            String previous_line = in.readLine();
            while (true) {
                // read two lines
                String current_line = in.readLine();

                // if current line is null, end file
                if (current_line == null) break;

                //StdOut.println("prev > " + previous_line + "\n" + "curr > " + current_line);
                StdOut.println("curr > " + current_line);

                previous_line = current_line;
            }
        }
    }
}