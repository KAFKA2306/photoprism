import { $config } from "app/session";
import { $gettext, T } from "common/gettext";

// 個人版は日本語だけをサポートする。
// options.FindLocale() は利用可能な言語が見つからない場合に先頭要素へ
// fallback するため、ブラウザ言語・保存値・?locale= の値にかかわらず ja へ収束する。
export let Options = [
  {
    text: "日本語",
    value: "ja",
  },
];

// 現在のロケールと Vuetify 用メッセージを返す。
export const Locale = () => {
  const locale = $config.getLanguageLocale();

  return {
    locale,
    fallback: "ja",
    rtl: { ja: false },
    messages: { [locale]: Messages(T) },
  };
};

// Vuetify UI の翻訳対象。
export const Messages = ($gettext) => {
  return {
    badge: $gettext("Badge"),
    open: $gettext("Open"),
    close: $gettext("Close"),
    dismiss: $gettext("Dismiss"),
    confirmEdit: {
      ok: $gettext("OK"),
      cancel: $gettext("Cancel"),
    },
    dataIterator: {
      noResultsText: $gettext("No matching records found"),
      loadingText: $gettext("Loading items..."),
    },
    dataTable: {
      itemsPerPageText: $gettext("Rows per page:"),
      itemsPerPageAll: $gettext("All"),
      ariaLabel: {
        sortDescending: $gettext("Sorted descending."),
        sortAscending: $gettext("Sorted ascending."),
        sortNone: $gettext("Not sorted."),
        activateNone: $gettext("Activate to remove sorting."),
        activateDescending: $gettext("Activate to sort descending."),
        activateAscending: $gettext("Activate to sort ascending."),
      },
      sortBy: $gettext("Sort by"),
    },
    dataFooter: {
      itemsPerPageText: $gettext("Items per page:"),
      itemsPerPageAll: $gettext("All"),
      nextPage: $gettext("Next page"),
      prevPage: $gettext("Previous page"),
      firstPage: $gettext("First page"),
      lastPage: $gettext("Last page"),
      pageText: $gettext("{0}-{1} of {2}"),
    },
    dateRangeInput: {
      divider: $gettext("to"),
    },
    datePicker: {
      itemsSelected: $gettext("{0} selected"),
      range: {
        title: $gettext("Select dates"),
        header: $gettext("Enter dates"),
      },
      title: $gettext("Select date"),
      header: $gettext("Enter date"),
      input: {
        placeholder: $gettext("Enter date"),
      },
    },
    noDataText: $gettext("No data available"),
    carousel: {
      prev: $gettext("Previous visual"),
      next: $gettext("Next visual"),
      ariaLabel: {
        delimiter: $gettext("Carousel slide {0} of {1}"),
      },
    },
    calendar: {
      moreEvents: $gettext("{0} more"),
      today: $gettext("Today"),
    },
    input: {
      clear: $gettext("Clear {0}"),
      prependAction: $gettext("{0} prepended action"),
      appendAction: $gettext("{0} appended action"),
      otp: $gettext("Please enter OTP character {0}"),
    },
    fileInput: {
      counter: $gettext("{0} files"),
      counterSize: $gettext("{0} files ({1} in total)"),
    },
    fileUpload: {
      title: $gettext("Drag and drop files here"),
      divider: $gettext("or"),
      browse: $gettext("Browse Files"),
    },
    timePicker: {
      am: $gettext("AM"),
      pm: $gettext("PM"),
      title: $gettext("Select Time"),
    },
    pagination: {
      ariaLabel: {
        root: $gettext("Pagination Navigation"),
        next: $gettext("Next page"),
        previous: $gettext("Previous page"),
        page: $gettext("Go to page {0}"),
        currentPage: $gettext("Page {0}, Current page"),
        first: $gettext("First page"),
        last: $gettext("Last page"),
      },
    },
    stepper: {
      next: $gettext("Next"),
      prev: $gettext("Previous"),
    },
    rating: {
      ariaLabel: {
        item: $gettext("Rating {0} of {1}"),
      },
    },
    loading: $gettext("Loading..."),
    infiniteScroll: {
      loadMore: $gettext("Load more"),
      empty: $gettext("No more"),
    },
  };
};

// 個人版で管理画面等から動的に参照される追加翻訳語。
export const ExtraMessages = () => {
  $gettext("Search");
  $gettext("Refresh");
  $gettext("Delete");
  $gettext("Open");
  $gettext("Name");
  $gettext("Username");
  $gettext("Display Name");
  $gettext("Version");
  $gettext("Theme");
  $gettext("Labels");
  $gettext("Removed");
  $gettext("Database");
  $gettext("User");
  $gettext("Account");
  $gettext("Authentication");
  $gettext("Session");
  $gettext("Time");
  $gettext("Site URL");
  $gettext("Message");
  $gettext("Application");
  $gettext("Service");
};

// バックエンド通知の翻訳元。課金・会員・クラスタ専用メッセージは個人版では登録しない。
export const BackendMessages = () => {
  $gettext("Something went wrong, try again");
  $gettext("Unable to do that");
  $gettext("Changes could not be saved");
  $gettext("Could not be deleted");
  $gettext("%s already exists");
  $gettext("Not found");
  $gettext("File not found");
  $gettext("File too large");
  $gettext("Unsupported");
  $gettext("Unsupported type");
  $gettext("Unsupported format");
  $gettext("Originals folder is empty");
  $gettext("Selection not found");
  $gettext("Entity not found");
  $gettext("Account not found");
  $gettext("User not found");
  $gettext("Label not found");
  $gettext("Camera not found");
  $gettext("Lens not found");
  $gettext("Album not found");
  $gettext("Subject not found");
  $gettext("Person not found");
  $gettext("Face not found");
  $gettext("Not available in public mode");
  $gettext("Not available in read-only mode");
  $gettext("Please log in to your account");
  $gettext("Permission denied");
  $gettext("Upload might be offensive");
  $gettext("Upload failed");
  $gettext("Upload to %s failed");
  $gettext("No items selected");
  $gettext("Failed creating file, please check permissions");
  $gettext("Failed creating folder, please check permissions");
  $gettext("Could not connect, please try again");
  $gettext("Enter verification code");
  $gettext("Invalid verification code, please try again");
  $gettext("Invalid password, please try again");
  $gettext("Feature disabled");
  $gettext("No labels selected");
  $gettext("No albums selected");
  $gettext("No files available for download");
  $gettext("Failed to create zip file");
  $gettext("Invalid credentials");
  $gettext("Invalid link");
  $gettext("Invalid name");
  $gettext("Busy, please try again later");
  $gettext("Insufficient storage");
  $gettext("Quota exceeded");
  $gettext("Registration disabled");
  $gettext("Verified email required");
  $gettext("Changes successfully saved");
  $gettext("Album created");
  $gettext("Album saved");
  $gettext("Album %s deleted");
  $gettext("Album contents cloned");
  $gettext("File removed from stack");
  $gettext("File deleted");
  $gettext("Selection added to %s");
  $gettext("One entry added to %s");
  $gettext("%d entries added to %s");
  $gettext("One entry removed from %s");
  $gettext("%d entries removed from %s");
  $gettext("Account created");
  $gettext("Account saved");
  $gettext("Account deleted");
  $gettext("Settings saved");
  $gettext("Password changed");
  $gettext("Import completed in %d s");
  $gettext("Import canceled");
  $gettext("Indexing completed in %d s");
  $gettext("Indexing originals...");
  $gettext("Indexing files in %s");
  $gettext("Indexing canceled");
  $gettext("Removed %d files and %d photos");
  $gettext("Moving files from %s");
  $gettext("Copying files from %s");
  $gettext("Labels deleted");
  $gettext("Label saved");
  $gettext("Subject saved");
  $gettext("Subject deleted");
  $gettext("Person saved");
  $gettext("Person deleted");
  $gettext("File uploaded");
  $gettext("%d files uploaded in %d s");
  $gettext("Processing upload...");
  $gettext("Upload has been processed");
  $gettext("Selection approved");
  $gettext("Selection archived");
  $gettext("Selection restored");
  $gettext("Selection marked as private");
  $gettext("Albums deleted");
  $gettext("Zip created in %d s");
  $gettext("Permanently deleted");
  $gettext("%s has been restored");
  $gettext("Successfully verified");
};
