using System.IO;

namespace SharedCode
{
    public static class SharedFunctions
    {

        public static int GetCurrentPhase()
        {

            var filePath = System.IO.Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "Database", "currentPhase.txt");

            using (StreamReader sr = new StreamReader(filePath))
            {

                string? line = sr.ReadLine();
                if (int.TryParse(line, out int result))
                {
                    return result;
                }
                else
                {
                    throw new InvalidOperationException("The file is empty, the line is null, or it does not contain a valid integer.");
                }

            }
        }

        public static int GetSelectedPhase(HttpRequest request, int def)
        {
            int selectedPhase = int.TryParse(request.Query["p"], out var parsedValue) ? parsedValue : def;

            if (def != 0 && selectedPhase == 0)
            {
                return def;
            }
            return selectedPhase;
        }

        public static int GetSelectedRow(HttpRequest request)
        {
            int selectedRow = int.TryParse(request.Query["r"], out var parsedValue) ? parsedValue : -1;

            return selectedRow + 1;
        }

        public static List<List<string>> ReadFile(int selectedPhase, string fileName)
        {

            List<List<string>> content = new List<List<string>>();

            int lineLength;

            switch (fileName)
            {
                case "table.txt":
                    lineLength = 10;
                    break;
                case "tournaments.txt":
                    lineLength = 5;
                    break;
                case "matches.txt":
                    lineLength = 7;
                    break;
                case "goals.txt":
                    lineLength = 5;
                    break;
                default:
                    return content;
            }

            using (StreamReader sr = new StreamReader(System.IO.Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "Database",
  selectedPhase + fileName)))
            {
                string? line;
                while ((line = sr.ReadLine()) != null)
                {
                    string[] tarr = line.Split(";");

                    for (int i = 0; i < tarr.Length; i += lineLength)
                    {
                        List<string> sublist = new List<string>();

                        for (int j = 0; j < lineLength && i + j < tarr.Length; j++)
                        {
                            sublist.Add(tarr[i + j]);
                        }

                        content.Add(sublist);
                    }
                }
            }

            return content;

        }
    }
}