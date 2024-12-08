using System.IO;

namespace SharedCode
{
    public static class SharedFunctions
    {
        public static string GetGreeting(string name)
        {
            return $"Hello, {name}!";
        }

        public static int GetCurrentPhase(){

            int phase;

            var filePath = System.IO.Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "Database", "currentPhase.txt");

            using (StreamReader sr = new StreamReader(filePath))
            {

                return int.Parse(sr.ReadLine());

            }
        }
    }
}